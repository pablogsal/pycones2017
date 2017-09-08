See https://github.com/python/cpython/pull/3454

def namedtuple(typename, field_names, *, rename=False, module=None):
    ...

very down the path:

result = type(typename, (tuple,), class_namespace)

No more exec when creating namedtuples!! Now the namedtuples are created using the type metaclass directly.
