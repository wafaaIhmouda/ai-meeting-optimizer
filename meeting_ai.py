import sounddevice as sd
import numpy as np
import queue
import threading
import time
import requests
from faster_whisper import WhisperModel

# =========================
# CONFIG (optimized for 2B model)
# =========================

SAMPLE_RATE = 16000
CHUNK_SECONDS = 4              # small chunks = better accuracy
ANALYSIS_INTERVAL = 12         # don't overload Qwen 2B
MAX_BUFFER_CHUNKS = 12         # control context size

OLLAMA_MODEL = "qwen3.5:2b"

audio_queue = queue.Queue()
transcript_buffer = []

# =========================
# WHISPER (light + fast)
# =========================

whisper = WhisperModel(
    "small",          # better balance than base for meetings
    device="cpu",
    compute_type="int8"
)

# =========================
# OLLAMA CALL (IMPORTANT FIXED FORMAT)
# =========================

def call_qwen(transcript):
    prompt = f"""
You are an AI Meeting Assistant optimized for short context.

Analyze this meeting transcript:

{transcript}

Return EXACT format:

Summary:
Action Items:
Decisions:
Risks:
"""

    try:
        res = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=60
        )

        return res.json()["message"]["content"]

    except Exception as e:
        return f"Error calling Ollama: {e}"

# =========================
# AUDIO CAPTURE
# =========================

def audio_callback(indata, frames, time, status):
    audio_queue.put(indata.copy())

def audio_listener():
    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        callback=audio_callback
    ):
        print("🎤 Listening... (Ctrl+C to stop)")
        while True:
            time.sleep(1)

# =========================
# TRANSCRIPTION ENGINE
# =========================

def transcribe_loop():
    buffer = []

    while True:
        data = audio_queue.get()
        buffer.append(data)

        # convert chunks to seconds
        if len(buffer) >= int(CHUNK_SECONDS * SAMPLE_RATE / 1024):

            audio = np.concatenate(buffer, axis=0).flatten()
            buffer = []

            segments, _ = whisper.transcribe(audio, beam_size=5)

            text = " ".join(s.text for s in segments).strip()

            if text:
                print("📝", text)
                transcript_buffer.append(text)

                # keep buffer small (IMPORTANT for Qwen 2B)
                if len(transcript_buffer) > MAX_BUFFER_CHUNKS:
                    transcript_buffer.pop(0)

# =========================
# ANALYSIS ENGINE (Qwen)
# =========================

def analysis_loop():
    while True:
        time.sleep(ANALYSIS_INTERVAL)

        if not transcript_buffer:
            continue

        context = " ".join(transcript_buffer)

        print("\n🤖 Analyzing meeting...\n")

        result = call_qwen(context)

        print("\n======================")
        print("MEETING INSIGHT")
        print("======================")
        print(result)
        print("======================\n")

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    t1 = threading.Thread(target=audio_listener)
    t2 = threading.Thread(target=transcribe_loop)
    t3 = threading.Thread(target=analysis_loop)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()