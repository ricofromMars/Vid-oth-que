from os import system
import sys

def clear():
    if sys.platform == "win32":
        system('cls')
    else:
        system('clear')

def showMenu():
    print("Videotheque")
    print("-" * 11)
    print("1 - Afficher la liste des films par ordre alphabetique")
    print("2 - Afiicher la liste des films par dates de sortie")
    print("3 - Afficher la liste des films en fonction du support")
    print("4 - Afficher les films actuellement en pret")
    print("5 - Afficher la liste des amis")
    print("6 - Trouver un film")
    print("7 - Sortir")

if __name__ == "__main__":
    clear()
    