#Jarvis V2
import os
import speech_recognition as sr
import random
import detectwakeword #detectwakeword.py
import nltk
import json
import time
import wikipedia
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
with open('config.json', 'w+') as file:
    config = json.load(file)
with open('brain.json') as file:
    intents = json.load(file)
server = config['Server']
def generate_response(intent):
    out = random.choice(intent['responses'])
    if (not out == None):
        return(out) 
    else: 
        return("NONE")
def say(text):
    if not server:
        os.system(f"echo '{text}' | \
    piper --model en_US-lessac-medium.onnx --output-raw | \
    aplay -r 22050 -f S16_LE -t raw -")
    else:
        os.system(f"echo '{text}' | \
    piper --model en_US-lessac-medium.onnx --output_file output.wav")
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
        if config['OffStt'] == "True":
            from faster_whisper import WhisperModel
            model_size = "large-v3"
            model = WhisperModel(model_size, device="cuda", compute_type="float16")
            segments, info = model.transcribe("audio.mp3")
            for segment in segments:
                text = segment.text
                return segment.text
        else:
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


while(1):
    try:
        start()

    except KeyboardInterrupt:
        exit()
