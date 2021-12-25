from sortFunctions import dateSorting, nameSorting, rentSorting, typeSorting
from functions import clear, findMovie, friendsList, showMenu, get_friends_datas, get_movies_datas
from os import path

CUR_DIR = path.abspath(path.dirname(__file__))
DATAS_FILE = path.join(CUR_DIR, "datas", "datas.txt")

if __name__ == "__main__":
    
    # Recuperation des donnees brutes depuis le fichier datas.txt 
    # et mise en forme dans des dictionnaires
    movies = get_movies_datas(DATAS_FILE)
    friends = get_friends_datas(DATAS_FILE, movies)

    
    """ Corps du programme """
    while True:
        clear()
        showMenu()
        userChoice = input("-> ")

        if userChoice == "1":
            nameSorting(movies)
        elif userChoice == "2":
            dateSorting(movies)
        elif userChoice == "3":
            print("1 - Vhs")
            print("2 - Dvd")
            typeChoice = ""
            while typeChoice != "1" and typeChoice != "2":
                typeChoice = input("-> ")
            if typeChoice == "1":
                typeSorting(movies, "Vhs")
            else:
                typeSorting(movies, "Dvd")
        elif userChoice == "4":
            rentSorting(movies, friends)
        elif userChoice == "5":
            friendsList(friends)
        elif userChoice == "6":
            findMovie(movies, friends)
        elif userChoice == "7":
            break
        