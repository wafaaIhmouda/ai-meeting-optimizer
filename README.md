# AI Meeting Optimizer

## Overview

AI Meeting Optimizer is a Python-based application that captures live audio from a microphone, transcribes speech into text using **Faster Whisper**, and analyzes meeting conversations in real time using **Ollama** with the **Qwen 3.5 2B** language model.

The application automatically generates:

* 📝 Live meeting transcription
* 📄 Meeting summary
* ✅ Action items
* 📌 Decisions
* ⚠️ Risks

All processing is performed **locally**, meaning your meeting audio never leaves your computer and is not sent to any cloud AI service.

---

# Features

* 🎤 Real-time microphone recording
* 📝 Live speech-to-text transcription
* 🤖 AI-powered meeting analysis
* 📋 Automatic meeting summaries
* ✅ Action item extraction
* 📌 Decision tracking
* ⚠️ Risk identification
* 🔒 Fully offline using Ollama

---

# Technology Stack

* Python 3.11+
* Faster Whisper
* Ollama
* Qwen 3.5 2B
* NumPy
* SoundDevice
* Requests
* WebRTC Voice Activity Detection (optional)

---

# Project Structure

```text
ai-meeting-optimizer/
│
├── meeting_ai.py
├── README.md
├── requirements.txt
├── .gitignore
└── venv/
```

> **Note:** The `venv/` directory should never be uploaded to GitHub.

---

# Prerequisites

Before running the project, install the required software.

## 1. Install Python

Verify your Python installation:

```bash
python3 --version
```

If Python is not installed, download it from:

https://www.python.org/downloads/

---

## 2. Install Ollama

Download Ollama:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

---

## 3. Download the Qwen Model

Pull the model:

```bash
ollama pull qwen3.5:2b
```

Verify it has been downloaded:

```bash
ollama list
```

Expected output:

```text
qwen3.5:2b
```

---

# Clone the Repository

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-meeting-optimizer.git
```

Navigate into the project directory:

```bash
cd ai-meeting-optimizer
```

---

# Create a Virtual Environment

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it.

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```cmd
venv\Scripts\activate
```

If successful, your terminal will display:

```text
(venv)
```

---

# Install Project Dependencies

Install the required Python packages:

```bash
pip install faster-whisper sounddevice numpy scipy requests webrtcvad
```

If you're using **macOS** and `sounddevice` fails to install, first install PortAudio:

```bash
brew install portaudio
```

Then reinstall SoundDevice:

```bash
pip install sounddevice
```

---

# Verify Ollama is Running

Start the Ollama server:

```bash
ollama serve
```

If you receive:

```text
Error: listen tcp 127.0.0.1:11434: bind: address already in use
```

this means Ollama is already running, so you can continue.

---

# Running the Application

## Step 1: Navigate to the project directory

Before running the application, make sure you are inside the project folder.

If you cloned the repository:

```bash
cd ai-meeting-optimizer
```

Or, if the project already exists on your computer:

```bash
cd ~/ai-meeting-optimizer
```

Verify that you are in the correct folder:

```bash
ls
```

You should see:

```text
meeting_ai.py
README.md
requirements.txt
.gitignore
venv/
```

---

## Step 2: Activate the virtual environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```cmd
venv\Scripts\activate
```

---

## Step 3: Run the application

Run one of the following commands:

```bash
python meeting_ai.py
```

or

```bash
python3 meeting_ai.py
```

depending on your Python installation.

If everything is configured correctly, the terminal should display:

```text
🎤 Listening... (Ctrl+C to stop)
```

The application will then:

1. Capture audio from your microphone.
2. Convert speech into text using Faster Whisper.
3. Send the transcript to Ollama.
4. Generate:

   * Meeting Summary
   * Action Items
   * Decisions
   * Risks

---

# Example Meeting

Example meeting conversation:

> Good morning everyone. Today we will discuss the AI Meeting Optimizer project. Sarah will design the user interface. Mohammed will implement the backend integration. The first prototype should be be completed by next Friday.

Example AI output:

```text
Summary:
The team discussed the AI Meeting Optimizer project and assigned responsibilities.

Action Items:
- Sarah: Design the user interface.
- Mohammed: Implement the backend integration.

Decisions:
- Deliver the first prototype by next Friday.

Risks:
- Backend integration may require additional testing.
```

---

# Troubleshooting

## ModuleNotFoundError

Install the missing package:

```bash
pip install PACKAGE_NAME
```

Example:

```bash
pip install sounddevice
```

---

## Ollama Read Timeout

Error:

```text
Error calling Ollama: HTTPConnectionPool(host='localhost', port=11434): Read timed out.
```

Possible solutions:

* Verify Ollama is running.
* Check that the Qwen model has been downloaded.
* Reduce the transcript size before sending it to the model.
* Increase the timeout value in the Python code.
* Verify the model by running:

```bash
ollama run qwen3.5:2b
```

---

## No Transcription Appears

If the application displays:

```text
🎤 Listening...
```

but no transcription appears:

1. Ensure microphone permissions are enabled.

**macOS**

System Settings → Privacy & Security → Microphone

Enable access for:

* Terminal
* Visual Studio Code

2. Test whether audio is being received by temporarily printing debug messages inside the audio callback.

3. Verify that Faster Whisper has finished downloading its model during the first execution.

4. Speak clearly into the microphone for several seconds.

---

## Verify the Model

```bash
ollama list
```

Expected output:

```text
qwen3.5:2b
```

---

# Stop the Application

To stop the application, press:

```text
Ctrl + C
```

---

# Future Improvements

* Speaker diarization
* Google Meet integration
* Zoom integration
* Real-time streaming transcription
* AI meeting analytics dashboard
* Export meeting minutes to PDF
* Multi-language transcription
* Meeting search and retrieval

---
# Author

**Wafaa Ihmouda**

IT Teacher • Human-Computer Interaction Researcher • Educational Technology Enthusiast

**Research Interests**

* Human–Computer Interaction (HCI)
* Educational Technology
* Serious Games
* Artificial Intelligence
* Accessibility
* Meeting Intelligence Systems
