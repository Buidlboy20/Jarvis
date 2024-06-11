import os
import sys
print("Updating APT")
os.system("sudo apt update")
if sys.prefix != sys.base_prefix:
  ask = input("Use existing venv? Y/N")
  if ask == "Y"
    print("Using existing venv")
  else:
    ask = input("Please input venv activation path. (E.G. venv/bin/activate)")
    os.system("source " + ask)
else:
  print("No venv detected.")
  ask = input("A: Would you like to create a venv, or B: specify a venv activation path? (E.G. venv/bin/activate) A/B")
  if ask == "A":
    print("Creating new venv with name Jarvenv")
    print("Installing python3-venv dependancy (Password may be required)")
    os.system("sudo apt-get install python3-venv")
    os.system("cd")
    os.system("python3 -m venv Jarvenv")
    os.system("source Jarvenv/bin/activate")
    
    

os.system("python3 -m pip install speechRecognition nltk playsound gTTS weather2 wikipedia google transformers torch simpleaudio pygame pydub flask pyalsaaudio")
