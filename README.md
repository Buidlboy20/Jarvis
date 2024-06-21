# Jarvis 

Yep, this is Jarvis from the MCU.
I know that there are other projects out there that are MUCH better, but I wanted to create my one from scratch.
This is my first public project. I have been working on this locally for ~5 months, and decided to rebuild it and make it better on github. 

## Disclaimer

### Please don't use it yet, unless you know what you are doing!

I hope that if an error occurs, it won't affect anything important. :|

I have built this on a Linux machine, and it may not work out of the box.
It may work on Windows Subsytem for Linux though.
Microphone and Speaker required.

I use Python3.10, and I have not tested it on other versions.

python3-venv package needs to be installed!

## Installation
Create a venv:

``` sh
python3 -m venv Jarvis
```
Activate the venv:

``` sh
source Jarvis/bin/activate
```
Clone the repo.

cd into the repo.

``` sh
python3 Install.py
```
This will run the setup.

## Start at Boot setup:
``` sh
sudo nano /etc/systemd/system/Jarvis.service
```
Put this in it:
```
[Unit]
Description=Jarvis_Service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 ~/Jarvis/Jarvis.py
[Install]
WantedBy=multi-user.target
```
Ctrl+X and then Y 


```systemd enable Jarvis```

If all goes correctly, Jarvis should boot at start. (Or you can manually start it using python3 Jarvis.py)

Now reboot you system using:

``` sh
init 6
```



