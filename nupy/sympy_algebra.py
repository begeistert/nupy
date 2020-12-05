from sympy import sympify, symbols, diff


def evaluate(function, variable, value):
    x = symbols(variable)
    new_value = sympify(function).subs(x, value)
    return float(new_value)


def derive(function, variable):
    x = symbols(variable)
    return diff(function, x)
