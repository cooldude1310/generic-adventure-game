import math
import random
import time
import os
import utils


load = True
waitTime = 1/3
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



def main():
    playerName = input("Welcome to the dungeon! What is your name?\n").title()
    if playerName == "":
        playerName = "Sam Altman"  
    if "Altman" in playerName:
        print("Oh boy... \nThis is gonna be fun...")
        hardDifficulty = True
        if input("lets make a bet. If you win, I will buy you 64 gigs of ddr5 6000. If I win, you nuke 3 datacenters and buy me a 5090.\nWould you like to continue? (Y/n)").lower() == "n":
            print("Ok then, whatever boats your float.")
            return
    else: 
        print(f"Hello, {playerName}")
    time.sleep(3.5)
    utils.clrscreen()
    print("Your mission today will be to collect and destroy all of the extremley dangerous cybercubes.")
    time.sleep(waitTime)
    print("They look exactly like a normal Rubik's Cube to the normal eye, but they contain an aincient dark energy thant very few can see.")
    time.sleep(waitTime)
    utils.clrscreen()
    print("This will be a dangerous mission. If you'd like to back out now this is your chance.")


utils.loading()
utils.clrscreen()
main()