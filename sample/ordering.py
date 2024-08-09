from dataclasses import dataclass

from sample import predicate
from sample.currying import curry


@dataclass(frozen=True)
class Same:
    pass


predicate.negate(bool)  # even this unused line is needed to reproduce the bug :)


neutral = Same()


@curry
def add(augend: Same, addend: Same) -> Same:
    ...
