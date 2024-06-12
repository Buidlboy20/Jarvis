#Jarvis V2
import os
import speech_recognition as sr
import random
import detectwakeword
import nltk
import addons
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

global output
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    global output
    try:
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        output = text
        return text
    except sr.UnknownValueError:
        print("Sorry, I can not understand what you said.")
        output = ""
        return None
    except sr.RequestError:
        print("Sorry, my speech recognition service is unavailable.")
        output = ""
        return None




def match_intent(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]

    best_match = None
    best_score = 0

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = word_tokenize(pattern)
            pattern_tokens = [word.lower() for word in pattern_tokens if word.isalpha()]
            pattern_tokens = [word for word in pattern_tokens if word not in stopwords.words('english')]

            score = len(set(tokens) & set(pattern_tokens))  # Calculate overlap score

            if score > best_score:
                best_match = intent
                best_score = score

    if best_match:
        return best_match
    else:
        return None


def handle_input(text):
    intent = match_intent(text)
    print(intent)
    if intent:
        response = generate_response(intent)
        if (not response == "NONE"):
            print(response)
            say(response)
            executecommand(intent)
        else:
            executecommand(intent)
def start():
    global output
    output = detectwakeword.detect()
    if output:
        
        handle_input(recognize_speech(),)
    else:
        output = ""


while(1):
    try:
        start()

    except KeyboardInterrupt:
        exit()