import re

from base_types.atomic_types import String
from core.descriptors import Descriptor


class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.max_len = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.max_len:
            raise ValueError("To big")
        super().__set__(instance, value)


class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError("Invalid string")
        super().__set__(instance, value)


class SizedString(String, Sized): pass


class RegexString(String, Regex): pass


class SizedRegexString(SizedString, Regex): pass


if __name__ == '__main__':
    print(SizedRegexString.__mro__)
