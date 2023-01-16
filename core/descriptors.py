# type checking
class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Typed(Descriptor):
    ty = object

    def __int__(self, *args, **kwargs):
        super.__init__(*args , **kwargs)

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f'Expected {self.ty}')
        super().__set__(instance, value)
