import random
from os import system

def run():

    my_menu = menu()
    palabra = random.choice(my_menu())

    spaces = dibujar_espacios(palabra)

    jugar(imagen=0,spaces=spaces,palabra=palabra)

def dibujar_ahorcado(indice:int)->str:

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

    #print(type(IMAGES[indice])) #tipo str

    return IMAGES[indice]

def menu():
    print("**************************")
    print("***     BIENVENIDO     ***")
    print("1. ANIMALES")
    print("2. PLANETAS")
    print("3. LENGUAJES PROGRAMACIÓN")
    print("4. NAVEGADORES")
    print("5. MARCAS PC")

    opcion = int(input("Opcion -> "))
    #print(type(opcion))

    def select_topic()->list:
        print()
        animales = ["CONEJO","RINOCERONTE","JIRAFA","LEOPARDO","CEBRA","BUFALO","HORMIGA","COCODRILO","ELEFANTE","DELFIN","PATO","PERRO","GATO","CANGREJO","PULPO","TORTUGA","BALLENA","FOCA","OSO","ZORRO","KOALA","MONO","POLLO","VACA"]
        planetas = ["MERCURIO","VENUS","TIERRA","MARTE","JUPITER","SATURNO","URANO","NEPTUNO"]
        lengProg = ["JAVA","PYTHON","JAVASCRIPT","PHP","SWIFT","VISUALBASIC"]
        navegadores = ["VIVALDI","OPERA","EDGE","SAFARI","MOZILLA","CHROME"]
        marcasPc = ["ACER","DELL","HP","LENOVO","ASUS","MICRONET","LANIX","HYUNDAI","HUAWEI","MSI","APPLE","TOSHIBA"]
        if opcion==1:
            #print(type(animales))
            return animales
        if opcion==2:
            #print(type(planetas))
            return planetas
        if opcion==3:
            #print(type(lengProg))
            return lengProg
        if opcion==4:
            #print(type(navegadores))
            return navegadores
        if opcion==5:
            #print(type(marcasPc))
            return marcasPc
    return select_topic

def dibujar_espacios(palabra:str)->list:
    spaces = ["➖"]*len(palabra)
    #rint(type(spaces))
    return spaces

def jugar(imagen:int,spaces:list,palabra:str):
    while True:
            system("cls")
            for c in spaces:
                    print(c,end=" ")
            print(dibujar_ahorcado(imagen))
            letra = input("Letra -> ").upper()

            encontrado = False

            for i, c in enumerate(palabra):
                if c == letra:
                    spaces[i] = letra
                    encontrado = True

            if not encontrado:
                if imagen <= 6:
                    imagen += 1

            if "➖" not in spaces:
                system("cls")
                print("""
░██████╗░░█████╗░███╗░░██╗░█████╗░░██████╗████████╗███████╗
██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║░░██╗░███████║██╔██╗██║███████║╚█████╗░░░░██║░░░█████╗░░
██║░░╚██╗██╔══██║██║╚████║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░
╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝░░░██║░░░███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝""")
                break
                input()

            if imagen > 6:
                system("cls")
                print("""
██████╗░███████╗██████╗░██████╗░██╗░██████╗████████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝
██████╔╝█████╗░░██████╔╝██║░░██║██║╚█████╗░░░░██║░░░█████╗░░
██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║░╚═══██╗░░░██║░░░██╔══╝░░
██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝░░░██║░░░███████╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝""")
                break
                input()
