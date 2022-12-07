import random
from os import system

def run():
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

                    BD = ["DIEGO","CHRISTIAN","EDUARDO","JOHN","BRANDON"]

    word = random.choice(BD)
    spaces = ["_"]*len(word)
    attemps = 0

    while True:
        system("cls")
        for character in spaces:
                print(character,end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra:").upper()


        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        if not found:     
            if attemps <= 6:
                attemps += 1

        if "_" not in spaces:
            system("cls")
            print("GANASTE")
            break
            input()

        if attemps > 6:
            system("cls")
            print("PERDISTE")
            break
            input()

if __name__ == '__main__':
    run()
