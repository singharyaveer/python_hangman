import random

print("-----------------------------------------------------------")
print("                    Welcome to Hangman!                    ")
print("-----------------------------------------------------------")
print(" ")
print(" ")

# main game loop
def main() -> None:

    # dictionary containing all words and hints
    word_dict : dict[str:str] = {
        "elegant": "Stylish and graceful",
        "freedom": "The power to act, speak, or think without hindrance",
        "harmony": "Agreement or concord",
        "passion": "Strong and barely controllable emotion",
        "victory": "The defeat of an enemy or opponent",
        "journey": "The act of traveling from one place to another",
        "inspired": "Filled with the urge or ability to do or feel something",
        "treasure": "A quantity of precious metals, gems, or other valuable objects",
        "laughter": "The action or sound of laughing",
        "whisper": "To speak very softly using one's breath",
        "blossom": "A flower or a mass of flowers on a tree or bush",
        "mystery": "Something that is difficult or impossible to understand or explain",
        "fantasy": "The faculty or activity of imagining things, especially things that are impossible or improbable",
        "symphony": "An elaborate musical composition for full orchestra",
        "creative": "Relating to or involving the use of the imagination or original ideas",
        "adventure": "An unusual and exciting or daring experience",
        "brilliant": "Exceptionally clever or talented",
        "charming": "Pleasing or delightful",
        "happiness": "The state of being happy",
        "sparkling": "Shining brightly with flashes of light",
        "radiant": "Sending out light; shining or glowing brightly",
        "wonderful": "Inspiring delight, pleasure, or admiration; extremely good",
        "courageous": "Not deterred by danger or pain; brave",
        "fascinate": "Draw irresistibly the attention and interest of (someone)",
        "vibrant": "Full of energy and life",
        "captivate": "Attract and hold the interest and attention of; charm",
        "enchanted": "Under a spell; magical",
        "serenity": "The state of being calm, peaceful, and untroubled",
        "glistening": "Shining with a sparkling light",
        "effervescent": "Bubbling, fizzy; vivacious and enthusiastic",
        "admirable": "Deserving respect and approval",
        "whimsical": "Playfully quaint or fanciful, especially in an appealing and amusing way",
        "spectacular": "Beautiful in a dramatic and eye-catching way",
        "fantastic": "Extraordinarily good or attractive",
        "exquisite": "Extremely beautiful and, typically, delicate",
        "delightful": "Greatly pleasing or entertaining",
        "magnificent": "Very beautiful, elaborate, or impressive",
        "harmonious": "Forming a pleasing or consistent whole",
        "radiance": "Light or heat as emitted or reflected by something",
        "passionate": "Showing or caused by strong feelings or a strong belief",
        "inspiring": "Having the effect of inspiring someone",
        "celestial": "Belonging or relating to heaven",
        "glorious": "Having, worthy of, or bringing fame or admiration",
        "tranquil": "Free from disturbance; calm",
        "brilliance": "Intense brightness of light",
        "wanderlust": "A strong desire to travel",
        "ecstasy": "An overwhelming feeling of great happiness or joyful excitement",
        "majestic": "Having or showing impressive beauty or dignity",
        "enchantment": "A feeling of great pleasure; delight",
        "captivating": "Attracting and holding interest as if by a spell",
        "fascination": "The power to fascinate someone; the quality of being fascinating",
        "whispering": "Speaking in a soft voice, especially to avoid being overheard",
        "mystical": "Relating to mystics or religious mysticism",
        "splendid": "Magnificent; very impressive",
        "adventurous": "Willing to take risks or to try out new methods, ideas, or experiences",
        "enigmatic": "Difficult to interpret or understand; mysterious",
        "sparklingly": "In a sparkling manner; with glittering or flashing lights",
        "bewitching": "Enchanting; charming in a mysterious way",
        "serenely": "In a calm, peaceful, and untroubled manner",
        "exhilarating": "Making one feel very happy, animated, or elated",
        "radiantly": "In a radiant manner; with a glowing brightness",
        "blossoming": "Developing or maturing into something greater or more mature",
        "charismatic": "Exercising a compelling charm that inspires devotion in others",
    }

    play : str = "Y"
    chances : int = 6
    wrongCharsAndWordsGuessed : list[str]= []
    correctCharsGuessed : list[str] = []

    while play == "Y":

       word : str = random.choice(list(word_dict.keys()))
    
       while True:
           print_hangman(chances)
           print(f"Your word: {' '.join(returnPrintableWord(word,correctCharsGuessed))}")
           print(" ")
           print(f"Hint: {word_dict[word]}")
           print(" ")
           print(f"Your chances left: {chances}")
           print(" ")
           guess : str = input("Enter your guess (Letter or Word): ").lower()
           print(" ")
           

           if len(guess) > 1:
               if guess in wrongCharsAndWordsGuessed:
                    print(f"The word: {guess}, has already been guessed")
                    print("Try again")
                    continue
                
               elif guess == word:
                   print("YOU HAVE WON THE GAME")
                   print(f"THE WORD IS {word}")
                   del word_dict[word]
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
                       del word_dict[word]
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
