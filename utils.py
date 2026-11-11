import os
import time
import random


def clrscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

def loading(loadtime=random.randint(1,15), enabled=True):
    if enabled == True:
        loadicons = ["|","/","--","\\"]
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
