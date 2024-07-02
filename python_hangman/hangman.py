import random

print("-----------------------------------------------------------")
print("                    Welcome to Hangman!                    ")
print("-----------------------------------------------------------")
print(" ")
print(" ")

# main game loop
def main() -> None:

    #list of random words
    words : list[str] = [
        "animal", "beach", "candle", "desert", "effort",
        "friend", "garden", "honor", "island", "jungle",
        "kettle", "leader", "market", "nature", "office",
        "planet", "quartz", "reason", "season", "trophy",
        "unicorn", "vessel", "wonder", "yellow", "access",
        "butter", "crisis", "driver", "engine", "forest",
        "ground", "health", "income", "jacket", "keeper",
        "lesson", "museum", "nation", "object", "person",
        "quiver", "region", "school", "ticket", "useful",
        "vortex", "window", "youth", "action", "bridge",
        "custom", "doctor", "engine", "future", "growth",
        "hotel", "impact", "jewels", "kidney", "letter",
        "mythic", "notion", "outlet", "profit", "rescue",
        "signal", "tablet", "united", "voyage", "writer",
        "zenith", "advice", "bucket", "chance", "debate",
        "effort", "family", "garage", "honest", "import",
        "jigsaw", "knight", "liquid", "mentor", "number",
        "option", "policy", "ribbon", "spirit", "throne",
        "urgent", "victor", "whaler", "yields", "agency",
        "branch", "cousin", "dollar", "editor", "flavor",
        "guitar", "hunger", "injury", "kitten", "lawyer",
        "member", "normal", "origin", "pencil", "radius",
        "soccer", "temple", "update", "vision", "weapon",
        "yellow", "artist", "breath", "circle", "danger",
        "effect", "future", "gravel", "humane", "intent",
        "jumper", "kitchen", "legacy", "margin", "oceanic",
        "parcel", "quaint", "beauty", "canvas", "desire",
        "escape", "fabric", "galaxy", "helmet", "impact",
        "jargon", "kitten", "legacy", "motion", "object"
    ]


    
    play : str = "Y"
    chances : int = 6
    wrongCharsAndWordsGuessed : list[str]= []
    correctCharsGuessed : list[str] = []

    

    while play == "Y":

       word : str = random.choice(words)

       while True:
           print_hangman(chances)
           print(f"Your word: {returnPrintableWord(word,correctCharsGuessed)}")
           print(" ")
           print(f"Your chances left: {chances}")
           print(" ")
           guess : str = input("Enter your guess (Letter or Word): ").lower()
           

           if len(guess) > 1:
               if guess in wrongCharsAndWordsGuessed:
                    print(f"The word: {guess}, has already been guessed")
                    print("Try again")
                    continue
                
               elif guess == word:
                   print("YOU HAVE WON THE GAME")
                   print(f"THE WORD IS {word}")
                   words.remove(word)
                   wrongCharsAndWordsGuessed = []
                   correctCharsGuessed = []
                   chances = 6
                   play = playAgainEvent()
                   break
               
               else:
                   chances -= 1
                   if chances == 0:
                       print_hangman(chances)
                       print("You have lost the game")
                       print(f"The word was: {word}")
                       wrongCharsAndWordsGuessed = []
                       correctCharsGuessed = []
                       chances = 6
                       play = playAgainEvent()
                       break
                   else:
                       print("Wrong guess")
                       print("Try again")
                       wrongCharsAndWordsGuessed.append(guess)
                       continue
                   
           elif len(guess) == 1:
               if (guess in wrongCharsAndWordsGuessed) or (guess in correctCharsGuessed):
                    print(f"The letter: {guess}, has already been guessed")
                    print("Try again")
                    continue
               
               elif guess in word:
                   correctCharsGuessed.append(guess)
                   
                   if returnPrintableWord(word,correctCharsGuessed) == word:
                       print("YOU HAVE WON THE GAME")
                       print(f"THE WORD IS {word}")
                       words.remove(word)
                       wrongCharsAndWordsGuessed = []
                       correctCharsGuessed = []
                       chances = 6
                       play = playAgainEvent()
                       break
                   else:
                       print("Correct Guess")

                   
                   continue
               
               else:
                   chances -= 1
                   if chances == 0:
                       print_hangman(chances)
                       print("You have lost the game")
                       print(f"The word was: {word}")
                       wrongCharsAndWordsGuessed = []
                       correctCharsGuessed = []
                       chances = 6
                       play = playAgainEvent()
                       break
                   else:
                       print("Wrong guess")
                       print("Try again")
                       wrongCharsAndWordsGuessed.append(guess)
                       continue
                   
           else:
               print("Please enter a Letter or a Word")
               continue


# select hangman figure to print to console
def print_hangman(chances : int) -> None:
    stages = [
        """
           -----
           |   |
           |
           |
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   0
           |
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   0
           |   |
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   0
           |  /|
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   0
           |  /|\\
           |
           |
        --------
        """,
        """
           -----
           |   |
           |   0
           |  /|\\
           |  /
           |
        --------
        """,
        """
           -----
           |   |
           |   0
           |  /|\\
           |  / \\
           |
        --------
        """
    ]

    stages = stages[::-1]
    print(stages[chances])

# return word to print to console and word with chars correctly guessed
def returnPrintableWord(word: str, correctCharsGuessed : list[str]) -> str:
    s : str = ""
    for i in word:
        if i in correctCharsGuessed:
            s = s + i
        else:
            s = s + "_"

    return s


# event after game is over
def playAgainEvent() -> str:
    while True:
        p = input("Do you want to play again(Y/N): ").upper()
        if p == "Y" or p == "N":
            break
        else:
            print("Please enter Y or N.")
            continue

    return p

if __name__ == "__main__":
    main()