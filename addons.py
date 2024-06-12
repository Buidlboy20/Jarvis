import os
import json
with open("AddonRepo.json") as file:
    addons = json.load(file)


def enableaddon(addon):
    if not(addon in os.environ['EnAddons']):
        os.environ['EnAddons'] = os.environ['EnAddons'] + f" '{addon}'"
    else:
        print("Addon already installed.")
        

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
        print(\n + i + ": " + addons[i])
        print(\n + " Please choose a number:")
        ask = input("")
        
