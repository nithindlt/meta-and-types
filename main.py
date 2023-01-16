from base_types.num_types import PositiveInteger, PositiveFloat
from base_types.string_types import SizedRegexString
from core.meta_descriptor import Structure

if __name__ == '__main__':
    class Stock(Structure):
        name = SizedRegexString(maxlen=4, pat="[A-Z]+$")
        shares = PositiveInteger()
        price = PositiveFloat()


    print(Stock("DLT", 1, 0.1))
