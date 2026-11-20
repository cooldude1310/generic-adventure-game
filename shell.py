commands = {
    "help":{
        'action':"list avalable commands and what they do",
        'usage':"help"
    },
 #   "man":{
 #       'action':"explain in detail what a specific command does and its syntax"
 #   },
    "clear":{
        'action':"clears the screen.",
        'usage':"clear"
    },
    "exit":{
        'action':"exit your current shell.",
        'usage':"exit"
    },
    "ssh":{
        'action':"remote shell into another computer.",
        'usage':"ssh <remote username>@<remote ip address>"
    },
    "sudo pacman -S":{
        'action':"install packages and other software.",
        'usage':"sudo pacman -S <package name>"
    },
}

def help():
    for i in commands:
        if i != "gs":
            print(f"{i}")
            print(f"    run the command {i} to {commands[i]['action']}")
            print()
            print(f"    Usage: {commands[i]['usage']}")
            print()
        else:
            print("gs")
            print("    run the command gs to install games.")
            print()
            print("    Usage:")
            print("    gs -l to list all games")
            print("    gs -i <game name>")

def man(comm):
    print("access and print manpage for command <comm> from respective .txt")
