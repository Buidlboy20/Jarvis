import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import xml

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
    

import json
with open("AddonRepo.json") as file:
    addons = json.load(file)


def enableaddon(addon):
    if not(addon in os.environ['EnAddons']):
        os.environ['EnAddons'] = os.environ['EnAddons'] + f" '{addon}'"
    else:
        print("Addon already installed.")
def intentcheck(output):
    for i in os.environ['EnAddons']:
        match_intent(output)
def installaddon(addonnum):
    addon = listaddons[addonnum]
    if addon == "TpLink-kasa":
        os.system("pip install python-kasa")
        enableaddon(addon)
    elif addon == "Roku":
        os.system("pip install roku")
        from roku import Roku
        roku = Roku()
        for i in roku.discovery():
        

            import requests
            import xmltodict
            url = roku.discovery()[i]
            response = requests.get(url)
            data = xmltodict.parse(response.content)
            data['root']['device']['friendlyname']


            

print("Activating Addon Installer")
os.system("sudo apt install git")
os.system(os.environ['JARVISVENVPATH'])
os.system("pip install gitpython")
import git
def gitclone(url):
    return git.Repo.clone_from(url)

ask = input("A: Install from official repo. B: Install from other repo. (May not be compatible) A/B ")
if ask == "A":
    for i in addons:
        print("\n" + i + ": " + addons[i])
        print("\n" + " Please choose a number:")
        ask = input("")
        addon2install = addons[ask]
        os.system("git clone " + addon2install + " addons/")
        os.system("python3 addons/setup.py")
        

