# J.A.R.V.I.S – Your Personal AI Voice Assistant in Python

A personal voice assistant built with **Python**, capable of performing a wide range of tasks — from opening applications, reading news, sending emails, playing music, checking the weather, to taking screenshots and even chatting interactively.

> Inspired by Marvel’s J.A.R.V.I.S, this assistant listens to your voice, understands your commands, and executes tasks like a true AI butler.

## Features

- Voice recognition (speech-to-text using `speech_recognition`)
- Text-to-speech with natural voices using `pyttsx3`
- Greet user based on time of day
- Open/close Notepad, Command Prompt, etc.
- Play random/specific music
- Search Google, Wikipedia, YouTube, Facebook
- Read the latest tech news (via NewsAPI)
- Send email and attach files
- Take screenshots and save them
- Report temperature using Google search
- Tell user's current location based on IP
- Check laptop battery percentage
- Perform speedtest for internet connection
- Access webcam
- Learn how to do something via WikiHow
- Small talk and conversation (basic)
- Download Instagram profile picture
- Infinite command loop unless told to stop

## 🛠️ Installation

### Requirements

Install all required Python libraries:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyautogui psutil speedtest-cli instaloader pywikihow beautifulsoup4 requests opencv-python PyPDF2
```

> Ensure you also install `PyAudio`. If you get errors on Windows, try:

```bash
pip install pipwin
pipwin install pyaudio
```

## How to Run

```bash
python beta.py
```

Then say:

```
Jarvis
```

to wake it up and start giving voice commands!

You can also say:

```
Shut down
```

to exit.

## Example Commands

| Command                            | What it does                   |
| ---------------------------------- | ------------------------------ |
| "Open Notepad"                     | Launches Notepad               |
| "Play sad music"                   | Plays predefined sad song      |
| "What is my IP address?"           | Tells your public IP           |
| "Wikipedia Elon Musk"              | Reads 2-line Wikipedia summary |
| "Email to me"                      | Asks and sends email or file   |
| "Where am I?"                      | Finds your current location    |
| "Take a screenshot"                | Captures and saves screenshot  |
| "Open my laptop camera"            | Opens webcam                   |
| "Tell me the temperature in Hanoi" | Reads current temperature      |
| "Power"                            | Shows battery percentage       |
| "Internet speed"                   | Measures and announces speed   |
| "Instagram profile"                | Downloads IG profile picture   |
| "I want to make banana bread"      | Uses WikiHow to explain        |
| "No thanks"                        | Exits gracefully               |

## Project Structure

```
J.A.R.V.I.S/
├── beta.py                   # Main Python script (voice assistant)
├── Music/                    # Your local music folder
└── README.md                 # Project description
```

## Notes

* To use email features, replace the placeholders in:

  ```python
  server.login('your_email@gmail.com', 'your_password')
  ```

  and allow **"less secure apps"** (or generate App Password for Gmail).
* For News API, get your key at: [https://newsapi.org/](https://newsapi.org/)

## 👨‍💻 Author

* **Nguyễn Châu Tấn Cường** – Cre: \[UTE HCMUTE]

> This project was written for fun, learning, and demonstration of voice-controlled automation using Python.

## 📜 License

This project is open-source and free for educational or personal use. Commercial use is not permitted without permission.

```
