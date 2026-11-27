import utils
import time
import random
import shell
import shutil

name = "tung tung tung sahur"
fname = "brr brr patapim"
loadBool = False
pkgs = []
hashtags = "##############################################"

def pacman(package):
    if not package in pkgs:   
        print("resolving dependencies...")
        time.sleep(.125)
        print("looking for conflicting packages...")
        time.sleep(.125)
        print()
        print(f"Packages (1) gameshore-26.12.1")
        print()
        print(f"Total Installed Size: {random.uniform(1.3,5.79):.2f} GiB")
        print()
        proceed = input(":: Proceed with installation? [Y/n]").strip().capitalize()
        if proceed == "N":
            return
        else:
            print(f"(1/1) checking keys in keyring      [{hashtags}] 100%")
            time.sleep(.125)
            print(f"(1/1) checking package integrity        [{hashtags}] 100%")
            time.sleep(.125)
            print(f"(1/1) loading package files     [{hashtags}] 100%")
            time.sleep(.125)
            print(f"(1/1) checking for file conflicts       [{hashtags}] 100%")
            time.sleep(.125)
            print(f"(1/1) checking avalable disk space      [{hashtags}] 100%")
            time.sleep(.125)
            print(":: Processing package changes")
            time.sleep(.25)
            print(f"(1/1) installing {package}")
            time.sleep(.125)
            print(":: Running post-transition hooks...")
            time.sleep(.125)
            print("(1/4) Arming ConditionNeedsUpdate...")
            time.sleep(.125)
            print("(2/4) Refreshing PackageKit...")
            time.sleep(.125)
            print("(3/4) Updating icon theme caches...")
            time.sleep(.125)
            print("(4/4) Updating the desktop file MIME type cache...")
            time.sleep(.125)
            time.sleep(.125)
            pkgs.append(package)


def terminal(user,device):
    print("welcome to msh!\nfor a list of commands, type help")
    while True:
        prompt = input(f"[{user.lower()}@{device}] ~ ").strip()
        if prompt == "":
            print()
        else:
            lprompt = prompt.split()
            mcomm = lprompt[0]
            if prompt == "help":
                shell.help()
            elif "ssh rocky@192.168.42.73" == prompt:
                time.sleep(.125)
                terminal("rocky","portable-earth-thinking-machine")
            elif "man" == mcomm:
                shell.man(prompt.split())
            elif "clear" == mcomm:
                utils.clrscreen()
            elif "exit" == mcomm:
                return
            elif user == "rocky" and prompt == "sudo pacman -S gameshore":
                pacman("gameshore")
            else:
                print(f"msh: command not found: {mcomm}")
        
            

def playGame(introBool=True):
    if introBool == True:
        print("Welcome to CorpNet IT Helpdesk")
        utils.wait()
        name = input("What is your name?\n:").strip().title()
        while name == "" or name.isnumeric():
            if name.isnumeric():
                print("Do your parents not love you?")
                utils.wait()
            print("Invalid name. Please try again.")
            utils.wait(True)
            name = input("What is your name?\n:").strip().title()
        fname = name.split(maxsplit=1)[0]
        utils.clrscreen()
        print(f"Hi {name}!")
        utils.wait()
        print("You have a VERY VERY important task today.")
        utils.wait()
        print("Today you must help Rocky download GTA VI")
        utils.wait()
        print("He plans to take all of December off due to a *sudden* cold.")
        print("( ͠° ͟ʖ ͡°)")
        utils.wait()
        print("However, your client is approxamatley 16.3 light years away on Erid and the only connection you have to his computer is a remote shell.")
        utils.wait()
        print("You will have to SSH into his computer and install GTA VI using the GameShore CLI")
        utils.wait()
        print("He also uses Arch Linux [btw]")
        utils.wait()
        print("Just to clarify, he does know how to use pacman but he is actually having issues getting into his own computer.")
        utils.wait()
        print("At least he plans on paying you quite well.")
        utils.wait(True)
        print("You will need to use his package manager (pacman) to install the GameShore CLI.\n")
        utils.wait(True)
    terminal(fname, "office1-desktop")


utils.loading(loadBool)
playGame()
