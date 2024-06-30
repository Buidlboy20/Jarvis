#Jarvis V2
import os
import pygame
pygame.mixer.init()
import speech_recognition as sr
import random
import detectwakeword #detectwakeword.py
import nltk
import json
import time
import wikipedia
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
with open('config.json', 'r') as file:
    config = json.load(file)
with open('brain.json') as file:
    intents = json.load(file)

def generate_response(intent):
    out = random.choice(intent['responses'])
    if (not out == None):
        return(out) 
    else: 
        return("NONE")
def say(text):
    if not(config['Server'] == "True"):
        os.system(f"echo '{text}' | \
    piper --model en_GB-lessac-medium.onnx --output_file output.wav")
        pygame.mixer.music.load('output.wav')
        pygame.mixer.music.play()
    else:
        print("Server Output")
        os.system(f"echo '{text}' | \
    piper --model en_GB-lessac-medium.onnx --output_file output.wav")
        
global output
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    global output
    try:
        if config['OffStt'] == "True":
            with microphone as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=6).get_wav_data()
                from faster_whisper import WhisperModel
                print("Recognizing")
                model_size = "large-v3"
                model = WhisperModel(model_size, device="cpu", compute_type="int8")
                segments = model.transcribe(audio)
                for segment in segments:
                    text = segment.text
                    return segment.text
        else:
            with microphone as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=6)
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
    except sr.WaitTimeoutError:
        print("Timeout")
        output = ""
        return None
def executecommand(intent):
    intent = intent['tag']
    if intent['tag'] == 'time':
        t = time.strftime("%I:%M %p")
        print(t)
        say(f"the currert time is '{t}'", server)
        print("Executing time command...")



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
        
        handle_input(recognize_speech())
    else:
        output = ""

say("The 20 meter pacer test is a multi lung stage capacity test that gets more difficult as it continues. The 20 meter pacer test will begin in 30 seconds, line up at the start. The running speed starts slowly, but gets faster each time you hear this sound. A single lap should be completed after you hear this sound. Remember to run ina straight line, and for as long as possible. The test will begin on the word start. On your mark, get ready, START!")
while(1):
    try:
        start()

    except KeyboardInterrupt:
        exit()
