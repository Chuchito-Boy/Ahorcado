import random
from os import system


def run():
    IMAGES = ['''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱            🧱
    🧱            🧱
    🧱            🧱
    🧱            🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''', '''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱     😀     🧱
    🧱            🧱
    🧱            🧱
    🧱            🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''', '''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱     😀     🧱
    🧱     ❗     🧱
    🧱     ❗     🧱
    🧱            🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''', '''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱     🤨     🧱
    🧱   💪❗     🧱
    🧱     ❗     🧱
    🧱            🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''', '''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱     🤨     🧱
    🧱   💪❗👍   🧱
    🧱     ❗     🧱
    🧱            🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''', '''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱     🤨     🧱
    🧱   💪❗👍   🧱
    🧱     ❗     🧱
    🧱   🦶       🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''', '''
    🧱🧱🧱🧱🧱🧱🧱🧱
    🧱     ❗     🧱
    🧱     💀     🧱
    🧱   💪❗👍   🧱
    🧱     ❗     🧱
    🧱   🦶  🦵   🧱
    🧱            🧱
    🧱🧱🧱🧱🧱🧱🧱🧱''']

    BD = ["CONEJO","RINOCERONTE","JIRAFA","LEOPARDO","CEBRA","BUFALO","HORMIGA","COCODRILO","ELEFANTE","DELFIN","PATO","PERRO","GATO","CANGREJO","PULPO","TORTUGA","BALLENA","FOCA","OSO","ZORRO","KOALA","MONO","POLLO","VACA"]

    word = random.choice(BD)
    print()
    spaces = ["➖"]*len(word)
    attemps = 0

    while True:
            system("cls")
            for character in spaces:
                    print(character,end=" ")
            print(IMAGES[attemps])
            letter = input("Elige una letra: ").upper()


            found = False
            for idx, character in enumerate(word):
                if character == letter:
                    spaces[idx] = letter
                    found = True

            if not found:
                if attemps <= 6:
                    attemps += 1

            if "➖" not in spaces:
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