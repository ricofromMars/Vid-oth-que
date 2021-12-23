from functions import clear

def showList(movieList):
    clear()
    for movie in movieList:
        print(movie)
    print()
    input("Appuyez sur 'Entree'")


def dateSorting(movieDict):
    """ Tri les films par dates de sortie """
    dateList = []

    for item in movieDict.values():

        if not dateList:
            dateList.append(item)
        elif item.release >= dateList[-1].release:
            dateList.append(item)
        elif item.release <= dateList[0].release:
            dateList.insert(0, item)
        else:
            i = 0
            while i < len(dateList)-1:
                if (item.release >= dateList[i].release) and (item.release <= dateList[i+1].release):
                    dateList.insert(i+1, item)
                    break
                i += 1

    showList(dateList)

def nameSorting(movieDict):
    """ Tri les films par ordre alphabétiques """
    nameList = []

    for item in movieDict.values():

        if not nameList:
            nameList.append(item)
        elif item.name >= nameList[-1].name:
            nameList.append(item)
        elif item.name <= nameList[0].name:
            nameList.insert(0, item)
        else:
            i = 0
            while i < len(nameList)-1:
                if (item.name >= nameList[i].name) and (item.name <= nameList[i+1].name):
                    nameList.insert(i+1, item)
                    break
                i += 1

    showList(nameList)

def typeSorting(movieDict, vidType):
    """ Tri les films en fonction du support, Vhs ou Dvd """
    clear()
    typeList = []

    for item in movieDict.values():

        if item.type == vidType:
            print(item)
    print()
    input("Appuyez sur 'Entree'")

def rentSorting(movieDict, friendDict):
    """ Tri les films en fonction du statut de location """
    clear()
    for movie in movieDict.values():

        if movie.is_rent:
            """ Chercher à qui le film a été prêté """
            for friend in friendDict.values():
                if friend.movieTitle == movie.name:
                    print(f"{friend.name}: {movie.name}")
    print()
    input("Appuyez sur 'Entree'")