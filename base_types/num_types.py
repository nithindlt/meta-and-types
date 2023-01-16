from base_types.atomic_types import Integer, Float
from core.descriptors import Descriptor


class Positive(Descriptor):

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f'Must be >= 0')
        super().__set__(instance, value)


class PositiveInteger(Integer, Positive): pass


class PositiveFloat(Float, Positive): pass
