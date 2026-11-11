import math
import random
import time
import os


load = True
loadtime = random.randint(0,15)
loadicons = ["|","/","--","\\"]
hardDifficulty = False
seed = random.randint(1,1)
playerName = "Sam Altman"
## for items, the associated number is its strength
## for spells, the number is base damage also lvl is just a damage multiplier
stats = {
    "inventory": {
        "wand": 5,
        "apple": 10
    },
    "lvl": 1,
    "multiplier": 1,
    "spells": {
        "basic cast": 15
    },
    "hp": 35,
    "maxhp": 35
}

def clrscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

def loading():
    if load == True:
        for i in range(0,loadtime):
            for x in loadicons:
                clrscreen()
                print(f"Loading {x} \n {loadtime - i - 1} seconds remaining")
                time.sleep(1 / len(loadicons))

def heal(a):
    stats["hp"] += a
    if stats["hp"] > stats["maxhp"]:
        stats[hp] = stats["maxhp"]

def lvlup(b):
    stats["maxhp"] += b
    stats["lvl"] += 1

def room():
    print()

def main():
    playerName = input("Welcome to the dungeon! What is your name?\n").title()
    if playerName == "":
        playerName = "Sam Altman"  
    if "Altman" in playerName:
        print("Oh boy... \nThis is gonna be fun...")
        hardDifficulty = True
        if input("lets make a bet. If you win, I will buy you 64 gigs of ddr5 6000. If I win, you nuke 3 datacenters and buy me a 5090.\nWould you like to continue? (Y/n)").lower() == "n":
            return
    else: 
        print(f"Hello, {playerName}")
    time.sleep(3.5)
    clrscreen()
    print("Your mission today will be to collect and destroy all of the extremley dangerous cybercubes.")
    time.sleep(1/3)
    print("They look exactly like a normal Rubik's Cube to the normal eye, but they contain an aincient dark energy thant very few can see.")
    time.sleep(1/3)

loading()
clrscreen()
main()