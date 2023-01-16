from collections import OrderedDict
from inspect import Parameter, Signature

from core.descriptors import Descriptor


def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names)


class StructureMeta(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(cls, clsname, bases, cls_dict):
        # since ordered dict
        fields = [key for key, val in cls_dict.items()
                  if isinstance(val, Descriptor)]

        for descriptor_name in fields:
            cls_dict[descriptor_name].name = descriptor_name

        cls_obj = super().__new__(cls, clsname, bases, dict(cls_dict))

        sig = make_signature(fields)
        setattr(cls_obj, '__signature__', sig)
        return cls_obj


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({args})'
