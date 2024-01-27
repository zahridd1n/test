from abc import ABC,abstractmethod


class Transport(ABC):
    @abstractmethod
    def tanishtir(self):
        pass


class Avto(Transport):
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def tanishtir(self):
        return f"nomi:{self.name},rangi:{self.color}"

class Moto(Transport):
    def __init__(self,name,color):
        self.name=name
        self.color=color


class Bike(Transport):
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def tanishtir(self):
        return f"nomi:{self.name},rangi:{self.color}"
