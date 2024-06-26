import os
import time
import numpy as np
import pyaudio
from openwakeword.model import Model
from openwakeword.utils import download_models


def capture_single_audio_frame():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    try:

        data = stream.read(CHUNK)
        return data
    finally:

        stream.stop_stream()
        stream.close()
        p.terminate()

download_models(["hey_jarvis_v0.1.tflite"])


model = Model(wakeword_models=["hey_jarvis_v0.1.tflite"])

def detect():
    frame = capture_single_audio_frame()
    print("AudioFrameCaptured")
    audio_array = np.frombuffer(frame, dtype=np.int16)
    time.sleep(0.05)
    print("Predicting")
    output = model.predict(audio_array)
    if output['hey_jarvis_v0.1.tflite'] >= 0.0005:
        print("WakeWord Detected")
        output = None
        return True
    else:
        print(output['hey_jarvis_v0.1.tflite'])
        print("No wakeword")
        output = None
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
