class Positive:
    def __set_name__(self,owner,name):
        self.name = name
    def __get__(self,instance,owner):
        return instance.__dict__[self.name]
    def __set__(self,instance, value):
        if value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("The value is not positive")

import collections
class MetaAnnotations(type):
    @classmethod
    def __prepare__(metacls, name, base, **kwargs):
        return collections.ChainMap({},{"Positive":Positive})

    def __new__(meta,name,bases,kwargs):
        return super().__new__(meta,name,bases,kwargs.maps[0])

    def __init__(cls,name,bases,kwargs):
        for name,val in cls.__annotations__.items():
            desc = val()
            desc.__set_name__(cls,name)
            setattr(cls,name,desc)

class A(metaclass=MetaAnnotations):
    x : Positive

myobj = A()
myobj.x = 4
print(myobj.x)
myobj.x = -4
