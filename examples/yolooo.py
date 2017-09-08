def make_yoloooo(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as ex:
            print(f"{ex.__class__.__name__} supressed")
    return wrapper

class MetaYoloooo(type):
    def __new__(meta, base, names, kwargs):
        for name,attr in kwargs.items():
            if callable(attr):
                kwargs[name] = make_yoloooo(attr)
        return super().__new__(meta,base,names,kwargs)

class DefectiveCyborg(object,metaclass=MetaYoloooo):

    def __init__(self, name):
        raise ValueError

    def travel(self, destination, year):
        raise ZeroDivisionError

    def attack(self, target):
        raise RuntimeError

robot = DefectiveCyborg('T-1000')
robot.travel('Los Angeles', 1995)
robot.attack('Sarah Connor')
robot.attack('John Connor')
