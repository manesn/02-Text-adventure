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












































    # Huh? You're not supposed to be here. Did you look up something that doesn't exist?
    # I guess I can talk to you while you're here.
    # You can go ahead and call me crazy now, since I know you're gonna do it later.

    # This game contains some nods to some of my favorite games and fandoms out there, some more obvious than others.
    # And while it sounds childish, I sometimes imagine inserting myself into these worlds, and immersing myself into them.
    # For example, being able to visit Coruscant, the busy, bustling city planet in Star Wars, where the fabled Jedi Temple and the Galactic Senate are located, sounds like a dream to me.
    # Exploring these places, and being able to interact with everything... it would be awesome.

    # Everyone wonders what goes on in my head, and I can never truly answer them when they ask me.
    # It's just... an amalgamation of all the cool stuff I've ever seen, played, been to, etc., etc., and so forth.
    # I am an incredibly imaginative and creative person, partly due to my ADHD, which I am open about. It's made me who I am.
    # I wanted to make a game where this scenario would play out: what if someone was able to briefly enter my mind, and see what I see when my imagination begins to take over?
    # I've always wondered what imagination looks like for others, since I know everyone's different.
    # This is me showing just a snippet of what it looks like for me.

    # The area internally known as "MEMORYSPACE", is my "world of imagination".
    # All the places that the player visited before reaching "MEMORYSPACE", those help keep my imagination alive and constantly ever-changing.
    # New ideas and places stem from the games I've played, the books I've read, the movies and fandoms I've seen.
    # All of that feeds into imagination.
    # Some are totally original ideas, and then others take some inspiration from the ideas of others.
    # Since I was a kid, this place always existed for me.
    # I know everyone has their own "world of imagination", deep down there somewhere, even if they say they don't/aren't imaginative.
    
    # I believe most, if not all games, and even beyond that- movies, books, etc., have a foundation that is composed of imagination and creativity.
    # I don't see a game as just coding and programming.
    # I look at it more artistically.
    # Fandoms like Star Wars, Harry Potter, The Lord of the Rings, and games like Zelda, Xenoblade, UNDERTALE, etc...
    # They're all built on imagination being let loose, and creativity being expressed in it's raw form.
    # Characters, places, things... entire worlds and their stories are made from this.


    # What would games look like without imagination? What would the world look like without imaginative people?

    # thanks for listening to my spiel/rambling



    # and yes, i did listen to "Pure Imagination" while writing up the stuff for this game.