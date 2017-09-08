import collections
import collections
class MetaNoMoreInit(type):
    @classmethod
    def __prepare__(metacls, name, base, **kwargs):
        return collections.OrderedDict()
    def __new__(meta,name,bases,kwargs):
        if "__init__" not in kwargs:
            annotations = kwargs["__annotations__"]
            def __init__(self,*args,**kwargs):
                if args:
                    raise ValueError("Use only named arguments")
                self.__dict__.update(kwargs)

            kwargs["__init__"] = __init__
        return super().__new__(meta,name,bases,kwargs)

class Easy(metaclass=MetaNoMoreInit):
    x:int
    y:float
    z:str

myobj = Easy(x=1,y=3.4,z="Hello")
print(myobj.x)
print(myobj.y)
print(myobj.z)
