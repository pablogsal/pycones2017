class Meta42(type):
    def __new__(meta,name,bases,kwargs):
        return 42

class Cyborg42(metaclass=Meta42):
    pass

print(Cyborg42)

