class Movie:
    def __init__(self, name, release, status):
        self.name = name
        self.release = release
        self.is_rent = status

    def changeStatus(self, status):
        self.is_rent = status


class Vhs(Movie):
    def __init__(self, name, release, status=False):
        super().__init__(name, release, status)
        self.type = "Vhs"

    def __repr__(self):
        return f"{self.name}\nDate de sortie: {self.release}\nSupport: Vhs"

class Dvd(Movie):
    def __init__(self, name, release, status=False):
        super().__init__(name, release, status)
        self.type = "Dvd"

    def __repr__(self):
        return f"{self.name}\nDate de sortie: {self.release}\nSupport: Dvd"

class Friend:
    def __init__(self, name, movie=""):
        self.name = name
        self.movie = movie
    
    def __repr__(self):
        return f"{self.name}\n{self.movie}"