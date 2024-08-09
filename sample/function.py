from collections.abc import Callable

from sample.currying import curry

type Function[From, To] = Callable[[From], To]


@curry
@curry
def identity_compose[From, Intermediate, To](value: From, first: Callable[[From], Intermediate], second: Callable[[Intermediate], To]) -> To:
    ...


@curry
@curry
def neutral2[M](value: M, _: object, __: object) -> M:
    ...


@curry
@curry
@curry
def add[M, T](value: T, augend: Function[T, M], addend: Function[T, M], m_add: Callable[[M], Callable[[M], M]]) -> M:
    ...


add2 = identity_compose(add)(add)


@curry
def identity[T](_: object, value: T) -> T:
    ...
