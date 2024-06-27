import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import xml
with open("AddonRepo.json") as file:
    addons = json.load(file)

def installaddon(addonnum):
    addon2install = addons[addonnum]
    os.system("mkdir ~/Jarvis/addons")
    os.system("git clone " + addon2install + " /addons/")
    os.system("python3 addons/setup.py")
    with open("brain.json", 'w+') as jfile:
        existing_data = json.load(jfile)
        with open(f"/addons/'{addon2install}'"):
            print("WIP")

        


            

print("Activating Addon Installer")

ask = input("A: Install from official repo. B: Install from other repo. (May not be compatible) A/B ")
if ask == "A":
    for i in addons:
        print("\n" + i + ": " + addons[i])
        print("\n" + " Please choose a number:")
        ask = input("")

        

