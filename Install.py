import os
import sys
print("Updating APT")
os.system("sudo apt update")
if sys.prefix != sys.base_prefix:
  ask = input("Use existing venv? Y/N")
  if ask == "Y":
    print("Using existing venv")
  else:
    ask = input("A: Would you rather input venv activation path. (E.G. venv/bin/activate) B: Or would you rather create one? A/B")
    if ask == "A":
      ask = input("venv activation path:")
      os.system("source " + ask)
      os.environ['JARVISVENVPATH'] = "~/" + ask
    else:
      print("Creating new venv with name Jarvenv")
      print("Installing python3-venv dependancy (Password may be required)")
      os.system("sudo apt-get install python3-venv")
      os.system("cd")
      os.system("python3 -m venv Jarvenv")
      os.system("source Jarvenv/bin/activate")
      os.environ['JARVISVENVPATH'] = '~/Jarvenv/bin/activate'
else:
  print("No venv detected.")
  ask = input("A: Would you like to create a venv, or B: specify a venv activation path? (E.G. venv/bin/activate) A/B")
  if ask == "A":
    print("Creating new venv with name Jarvenv")
    print("Installing python3-venv dependancy (Password may be required)")
    os.system("sudo apt-get install python3-venv")
    os.system("cd")
    os.system("python3 -m venv ~/Jarvis/Jarvenv")
    os.system("source ~/Jarvis/Jarvenv/bin/activate")
    os.environ['JARVISVENVPATH'] = '~/Jarvenv/bin/activate'
#Install as a service.
  else:
    ask = input("venv activation path:")
    os.system("source " + ask)
    os.environ['JARVISVENVPATH'] = "~/" + ask
with open("/etc/systemd/system/Jarvis.service", "w") as file:
  file.write("""
[Unit]
Description=Jarvis_Service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 ~/Jarvis/Jarvis.py
[Install]
WantedBy=multi-user.target
""")
ask = input("Would you like you use the offline speech to text engine? Y/N ")
if ask == "Y":
  os.system("pip install faster-whisper")
  os.environ['OffStt'] = "True"
else:
  os.environ['OffStt'] = "False"
  
os.system("sudo systemctl daemon-reload -y")
os.system("sudo systemctl enable Jarvis.service -y")
os.system("sudo apt install python3-dev portaudio19-dev python3-pyaudio apt -y")
os.system("wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/northern_english_male/medium/en_GB-northern_english_male-medium.onnx?download=true")
os.system("wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/northern_english_male/medium/en_GB-northern_english_male-medium.onnx.json?download=true.json")
os.system("pip install --upgrade pip")
os.system("pip install speechRecognition nltk playsound gTTS weather2 wikipedia google transformers torch simpleaudio pygame pydub flask pyalsaaudio pyaudio")
