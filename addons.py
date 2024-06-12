import os
def listaddons():
    return [
        "TpLink-kasa",
        "spotify",
        "Roku"
    ]
def enableaddon(addon):
    if not(addon in os.environ['EnAddons']):
        os.environ['EnAddons'] = os.environ['EnAddons'] + f" '{addon}'"
    else:
        print("Addon already installed.")
        
def installaddon(addonnum):
    addon = listaddons[addonnum]
    if addon == "TpLink-kasa":
        os.system("pip install python-kasa")
