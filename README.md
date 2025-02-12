# Voice-Assistant-Using-Python

AI-Based Voice Assistant

This is a Python-based AI voice assistant that can recognize voice commands, perform web searches, manage tasks, play music, and more. It integrates speech recognition, text-to-speech, and automation features to provide a user-friendly experience.

Features

Voice Recognition: Uses Google Speech Recognition to convert spoken commands into text.

Text-to-Speech (TTS): Uses pyttsx3 for spoken responses.

Music Playback: Opens random YouTube music videos.

Time & Date Retrieval: Speaks the current time and date.

Task Management: Adds and retrieves to-do list tasks from a text file.

Application Control: Opens and closes applications.

Wikipedia Search: Retrieves and speaks short summaries from Wikipedia.

Web Browsing: Opens YouTube, Google search, and other websites.

WhatsApp Messaging: Sends WhatsApp messages using pywhatkit.

Email Sending: Sends emails using SMTP.

Weather Information: Fetches and speaks weather updates.

YouTube Video Search & Play: Searches and plays videos on YouTube.

Media Control: Stops or resumes YouTube videos and closes browser tabs.

Requirements

Install the necessary Python packages using:

pip install pyttsx3 SpeechRecognition plyer pyautogui wikipedia pywhatkit mtranslate psutil smtplib ssl

Ensure that your system has a microphone and internet connection for full functionality.

Usage

Run the script:

python main.py

Then, use voice commands like:

"Hello"

"Play music"

"What time is it?"

"Open Chrome"

"Search Wikipedia for Python programming"

"Send WhatsApp message"

"Check the weather in New York"

"Play a video on YouTube"
