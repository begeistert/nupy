from sympy import sympify, symbols


def eval(function, variable, value):
    x = symbols(variable)
    new_value = sympify(function).subs(x, value)
    return float(new_value)
