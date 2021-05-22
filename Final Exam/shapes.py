from os import kill


class Circle:
    def __init__(self, rad=1, high=1):
        self.__radius = rad

    def setRad(self, rad):
        if rad < 0.0 or rad > 100.0:
            kill
        else:
            self.__radius = rad


    def getArea(self):
        pi = 3.141592
        return ((int(self.__radius)**2) * pi)

    def __str__(self):
        return("The radius is: " + str(self.__radius)
        + " The Area is: " + str(self.getArea()))

