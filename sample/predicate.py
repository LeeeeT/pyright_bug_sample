from sample import function

function.identity(...)  # even this unused line is needed to reproduce the bug :)

negate = function.identity_compose(bool)
