from types import MappingProxyType
class MetaRegister(type):

    _registry = dict()

    def __new__(meta, name, bases, kwargs):
        kwargs["_registry"] = MappingProxyType(meta._registry)
        cls = super().__new__(meta,name,bases,kwargs)
        meta._registry[name] = cls
        return cls

class Cyborg(object,metaclass=MetaRegister):
    pass

class Ninja(object):
    pass

class CyborgNinja(Cyborg,Ninja):
    pass

print(MetaRegister._registry)
print(CyborgNinja._registry)


# Libraries that uses this pattern: SQLAlchemy, Ansible, Luigy...
