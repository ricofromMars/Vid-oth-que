from cleanDatas import cleanMovieDatas, cleanFriendsDatas
from sortFunctions import dateSorting, nameSorting, rentSorting, typeSorting
from functions import clear, showMenu

films = [
    ("Blade Runner (1982)", "vhf"),
    ("Alien : Le 8ème Passager (1979)", "vhf"),
    ("2001 : L'Odyssée de l'espace (1968)", "VhF"),
    ("Matrix (1999)", "DVD"),
    ("Interstellar (2014)", "dvD"),
    ("L'Empire contre-attaque (1980)", "vhf"),
    ("Retour vers le futur (1985)", "vhf"),
    ("La Guerre des Étoiles (1977)", "vhf"),
    ("L'Armée des 12 singes (1995)", "dVd"),
    ("Terminator 2 : Le Jugement dernier (1991)", "DVD"),
]

amis = [
    ("Paul", "Blade Runner"),
    ("Lucie",),
    ("Zoé", "Terminator 2 : Le Jugement dernier"),
]

if __name__ == "__main__":
    
    movies = cleanMovieDatas(films)
    friends = cleanFriendsDatas(amis, movies)
    
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
            pass
        elif userChoice == "6":
            pass
        elif userChoice == "7":
            break
        