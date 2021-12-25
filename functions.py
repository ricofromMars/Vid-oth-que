from os import system
import sys

from classes import Vhs, Dvd

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

def get_title(element):
    i = 1
    title = ""
    while element[i] != "(":
        title += element[i]
        i += 1
    return title.strip()

def get_release(element):
    
    i = element.index("(")
    return element[i+1:i+5]

def get_support(element):
    element = element.replace('"', '').strip()
    if element.lower() == "vhf":
        return "Vhs"
    else:
        return "Dvd"

def get_movies_datas(pathDatas):
    movies = {}
    with open(pathDatas, "r") as f:
        datas = f.readlines()
    del datas[0]
    for element in datas:
        if "amis" in element:
            i = datas.index(element)
            break
    del datas[i-2:]

    for element in datas:
        element = element.strip().lstrip("(").rstrip("),")
        elements = element.split(",")
        title = get_title(elements[0])
        release = get_release(elements[0])
        support = get_support(elements[1])

        if support == "Vhs":
            movies[title] = Vhs(name=title, release=int(release))
        else:
            movies[title] = Dvd(name=title, release=int(release))

    return movies


def get_friends_datas(pathDatas):
    pass