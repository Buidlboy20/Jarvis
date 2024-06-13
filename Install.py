import os
import sys
os.system("source")
print("Updating APT")
os.system("sudo apt update")
if not sys.prefix != sys.base_prefix:
  print("Warning! No venv detected.")
  exit()
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
  
os.system("sudo systemctl daemon-reload ")
os.system("sudo systemctl enable Jarvis.service ")
os.system("sudo apt install python3-dev portaudio19-dev python3-pyaudio pip -y")
os.system("wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/northern_english_male/medium/en_GB-northern_english_male-medium.onnx?download=true")
os.system("wget https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/northern_english_male/medium/en_GB-northern_english_male-medium.onnx.json?download=true.json")
os.system("pip install --upgrade pip")
os.system("pip install speechRecognition nltk playsound gTTS weather2 wikipedia google transformers torch simpleaudio pygame pydub flask pyalsaaudio pyaudio")
