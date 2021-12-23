from classes import Friend, Vhs, Dvd

def cleanMovieDatas(movie_list):
    """ Nettoie et formatte les données des films puis retourne un dictionnaire d'objets Movie """
    movies = {}
    for datas in movie_list:
        # extraire nom et date
        i = 0
        name = ""
        date = ""
        while (datas[0][i]) != "(":
            name += datas[0][i]
            i += 1
        i += 1
        name = name.rstrip()
        while (datas[0][i]) != ")":
            date += datas[0][i]
            i += 1

        # extraire et formatter le type de support
        type = datas[1]
        if type.lower() == "vhf":
            type = "Vhs"
        elif type.lower() == "dvd":
            type = "Dvd"

        # Créer et insérer les objets dans le dictionnaire
        if type == "Vhs":
            movies[name] = Vhs(name, int(date))
        else:
            movies[name] = Dvd(name, int(date))

    return movies

def cleanFriendsDatas(friend_list):
    """ Nettoie et formatte les données des amis et retourne un dictionnaire"""
    friends = {}
    name = ""

    for datas in friend_list:
        name = datas[0].capitalize()
        try:
            friends[name] = Friend(name=name, movie=datas[1])
        except IndexError:
            friends[name] = Friend(name=name)

    return friends