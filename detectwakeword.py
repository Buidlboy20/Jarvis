import os
import time
import numpy as np
import pyaudio
from openwakeword.model import Model
from openwakeword.utils import download_models


def capture_single_audio_frame():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16()
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    try:
        # Read a single audio frame
        data = stream.read(CHUNK)
        return data
    finally:
        # Clean up
        stream.stop_stream()
        stream.close()
        p.terminate()

# One-time download of all pre-trained models (or only select models)
download_models(["hey_jarvis_v0.1.tflite"])

# Instantiate the wake word detection model
model = Model(wakeword_models=["hey_jarvis_v0.1.tflite"])

def detect():
    while True:
        frame = capture_single_audio_frame()
        audio_array = np.frombuffer(frame, dtype=np.int16)
        time.sleep(0.05)
        output = model.predict(audio_array)
        if output['hey_jarvis_v0.1.tflite'] >= 0.0005:
            print("WakeWord Detected")
            return True
        else:
            print("No wakeword")
            return False
def detectfromfile(file):
    with open(file, 'rb') as file:
        audio_array = np.frombuffer(file, dtype=np.int16)
        time.sleep(0.05)
        output = model.predict(audio_array)
        if output['hey_jarvis_v0.1.tflite'] >= 0.0005:
            return True
        else:
            return False
