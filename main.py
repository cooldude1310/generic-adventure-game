import random
import time
import utils
import mechs

loadBool = True
waitTime = 5
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



def intro():
    playerName = input("Welcome to the dungeon! What is your name?\n").strip().title()
    if playerName == "":
        playerName = "Sam Altman"  
    if "Altman" in playerName:
        print("Oh boy... \nThis is gonna be fun...")
        hardDifficulty = True
        if input("lets make a bet. If you win, I will buy you 64 gigs of ddr5 6000. If I win, you nuke 3 datacenters and buy me a 5090.\nWould you like to continue? (Y/n)").strip().lower() == "n":
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
    if input("Would you like to continue? (Y/n)").strip().lower() == "n":
        print("That's too bad. Maybe we can try again another time.")
        time.sleep(waitTime)
        print("Bye!")
        return
    print("Ok!")
    time.sleep(waitTime)
    utils.clrscreen()
    room1()

def room1():
    print("Welcome to the first room. There are 3 chests in the middle of the room.")
    time.sleep(waitTime)
    print("There are also two doors in the back.")
    time.sleep(waitTime)
    print("You will have to leave through one of the doors but you have the option to open just one chest.")
    while not choice in [1,2,3,4]:
        choice = input("""
            What would you like to do?
            1. Leftmost chest
            2. Middle chest
            3. Rightmost chest
            4. Leave without opening a chest
            
            **please enter a number 1-4**
            """).strip().int()
        if choice in [1,2,3,4]:
            utils.clrscreen()
            if  choice == 4:
                choice = -1 * pi
                
                print("You have chosen to leave the first room without opening a loot chest.")
            elif choice == 3:
                print("You have chosen to open the rightmost chest. ")

            elif choice == 2:
                print("You have chosen to open the middle chest.")
            elif choice == 1:
                print("You have chosen to open the leftmost chest. ")    
        else:
            utils.clrscreen()
            print(f"Invalid response {choice}\nPlease enter an integer between 1 and 4.")

utils.loading(loadBool)
utils.clrscreen()
intro()
