import speech_recognition as sr
import webbrowser
import pyttsx3
import Music_Library
import requests
from ai_client import ai_respond  




recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api="USE-YOUR-APIKEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram.")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        Music_Library.music[song]
        link=Music_Library.music[song]
        webbrowser.open(link) 

    elif "news" in command.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?q=technology&apiKey={news_api}")
            data = r.json()
            print("📦 API Response:", data)  # DEBUG

            articles = data.get("articles", [])
            if not articles:
                speak("Sorry, no news found.")
            else:
                speak("Here are the top 5 news headlines:")
                for article in articles[:5]:
                    print(article['title'])  # Debug
                    speak(article['title'])

        except Exception as e:
            print(f"❌ Error: {e}")
            speak("Something went wrong while fetching news.")


    else:
        try:
            speak("Let me think...")
            response = ai_respond(command)
            print("🤖 AI:", response)
            speak(response)
        except Exception as e:
            print("AI error:", e)
            speak("Sorry, I couldn't connect to the AI.")


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("🎤 Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                trigger = recognizer.recognize_google(audio)
                
                if "jarvis" in trigger.lower():
                    speak("Yes boss, what should I do?")
                    print("🎤 Listening for your command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print("✅ Command:", command)
                    process_command(command)
        except Exception as e:
            print(f"❌ Error: {e}")

