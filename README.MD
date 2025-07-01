## Jarvis AI Assistant
Jarvis is an intelligent, voice-controlled virtual assistant built to handle everyday tasks such as browsing the web, playing media, answering questions, and more. It leverages the power of OpenAI's GPT-3.5-turbo model (upgradeable) to provide smart and natural interactions.

> Jarvis is designed to be lightweight, customizable, and expandable — perfect for personal projects or smart desktop assistants.




## ✨ Key Features

### 🗣️ Voice Command Detection

* Listens actively for the wake word **"Jarvis"**.
* Uses the `speech_recognition` library to capture and interpret spoken commands.

### 🔊 Speech Output (Text-to-Speech)

* Speaks responses using `pyttsx3` for offline/local audio generation.
* Optionally supports `gTTS` and `pygame` for higher quality online voice playback.

### 🌐 Smart Web Navigation

* Opens popular sites like **Google**, **YouTube**, **LinkedIn**, and more via voice input.
* Automatically detects and formats spoken website names into valid URLs.

### 🧠 AI Interaction via OpenAI

* Integrated with OpenAI’s `GPT` models to answer user questions intelligently.
* Capable of handling casual conversation, general knowledge queries, and personalized responses.
* Mimics virtual assistants like **Alexa**, **Siri**, or **Google Assistant**.

## Dependencies
- SpeechRecognition (v3.14.3)
- pyttsx3 (v2.98)
- openai (v1.93.0)
- PyAudio (v0.2.14)
