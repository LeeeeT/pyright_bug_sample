from collections.abc import Callable


def curry[First, *Rest, Result](function: Callable[[First, *Rest], Result]) -> Callable[[*Rest], Callable[[First], Result]]:
    ...
