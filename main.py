#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game file. Ooooooooooooops.")
        os._exit(1)


def render(game,current):
    c = game[current]
    print("You are " + c["name"])
    print(c["desc"])

def get_input():
    response = input("Where do you wanna go?")
    response = response.upper().strip()
    return response

def update(game,current,response):
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]
    return current
    

# The main function for the game
def main():
    current = 'START'  # The starting location
    end_game = ['END']  # Any of the end-game locations

    game = load_files()

    while True:
        render(game,current)

        for e in end_game:
            if current == e:
                print("''There is no life I know like pure imagination... living there, you'll be free... if you truly wish to be.'' Nick said, smiling. \n''Our imagination is what makes our games games, and our dreams dreams. Without it... we would have nothing.'' he said. ''You just witnessed first hand how my imagination made a game. Thanks for playing along with me.''")
                break #break out of the while loop

        response = get_input()

        if response == "QUIT" or response == "Q":
            break #break out of the while loop

        current = update(game,current,response)

    print("Everything goes dark, and the dream... ends abruptly. You wake up. Looking around. You were at a desk, alone, your computer off. What could have happened? You may never know now that you've done what you did.")

# run the main function
if __name__ == '__main__':
	main()