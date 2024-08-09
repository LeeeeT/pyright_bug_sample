from dataclasses import dataclass

from sample import predicate
from sample.currying import curry


@dataclass(frozen=True)
class Same:
    pass


predicate.negate(bool)


neutral = Same()


@curry
def add(augend: Same, addend: Same) -> Same:
    ...
