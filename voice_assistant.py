import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import datetime
import os

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

openai.api_key = 'your-openai-api-key-here'

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please repeat.")
        return None
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None

def process_command(command):
    if command is None:
        return

    if 'open' in command:
        if 'google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif 'telegram' in command:
            webbrowser.open("https://www.telegram.org")
            speak("Opening telegram")
            
        else:
            app_name = command.replace('open', '').strip()
            open_application(app_name)

    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")  

    elif 'date' in command:
        today = datetime.datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(url)
        speak(f"Searching for {search_query}")

    elif 'question' in command or 'answer' in command:
        question = command.replace('question', '').replace('answer', '').strip()
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        speak(answer)

    elif 'play' in command:
        song = command.replace('play', '').strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
        speak(f"Playing {song} on YouTube")

    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

def open_application(app_name):
    if 'notepad' in app_name:
        os.system('notepad')
        speak("Opening Notepad")
    elif 'calculator' in app_name:
        os.system('calc')
        speak("Opening Calculator")
    else:
        speak(f"Sorry, I don't know how to open {app_name}")

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()
