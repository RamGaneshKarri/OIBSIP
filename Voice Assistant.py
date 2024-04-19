import threading
import speech_recognition as sr
import datetime
import webbrowser
import random

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("User:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you please repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error processing your request. Please try again later.")
        return ""

def greet():
    responses = ["Hi there!", "Hello!", "Greetings!", "Hey!"]
    print(responses[random.randint(0, len(responses) - 1)])

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print("Current time is", current_time)

def search(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)
    print("Here are the search results for", query)

def process_command(command):
    if "hello" in command:
        greet()
    elif "time" in command:
        get_time()
    elif "search" in command:
        search(command.replace("search", "").strip())
    elif "exit" in command:
        print("Goodbye!")

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            threading.Thread(target=process_command, args=(command,)).start()
