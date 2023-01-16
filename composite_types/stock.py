from base_types.atomic_types import String
from base_types.num_types import PositiveInteger, PositiveFloat
from core.meta_descriptor import Structure


class Stock(Structure):
    _fields = ['name', 'shares', 'price']

    name = String('name') 
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')
