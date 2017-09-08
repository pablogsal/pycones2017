from abc import ABCMeta, abstractmethod

class MetaCyborg(metaclass=ABCMeta):
    @abstractmethod
    def travel(self, destination, year):
        ...

    @abstractmethod
    def attack(self, target):
        ...


class PrototypeCyborg(MetaCyborg):
    def __init__(self, name):
        self.name = name

    def travel(self, destination, year):
        print("Traveling really far")

class Cyborg(MetaCyborg):

    def __init__(self, name):
        self.name = name

    def travel(self, destination, year):
        print("Traveling really far")

    def attack(self,target):
        print("Atacking really hard")

robot = Cyborg('T-1000')
#This doesn't work
robot = PrototypeCyborg('T-1000')

