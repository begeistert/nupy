from nupy.algebra import evaluate
from pandas import DataFrame, set_option


def __configure__():
    set_option("display.precision", 20)
    set_option('colheader_justify', 'center')


def intermediate_value(function, variable, intervals, tolerance=1e-10, limit=250, just_root=False):
    __configure__()
    iterations = {
        'a_n': [],
        'b_n': [],
        'p_n': [],
        'f_n': []
    }
    header = ['a_n', 'b_n', 'p_n', 'f_n']
    fa_1 = intervals[0]
    fb = intervals[1]
    pn_1 = sum(intervals) / 2
    condition = evaluate(function=function, variable=variable, value=fa_1) * evaluate(function=function,
                                                                                      variable=variable, value=fb)
    iteration_1 = 0
    if condition < 0:
        while True:
            if iteration_1 == 0:
                fn_1 = evaluate(function=function, variable=variable, value=pn_1)
                fx_1 = evaluate(function=function, variable=variable, value=fa_1) * fn_1

                # iterations.append([iteration_1, intervals[0], intervals[1], pn_1])
                # iterations['Iteration'].append(iteration_1)
                iterations['a_n'].append(intervals[0])
                iterations['b_n'].append(intervals[1])
                iterations['p_n'].append(pn_1)
                iterations['f_n'].append(evaluate(function=function, variable=variable,
                                                  value=pn_1))
                if fx_1 < 0:
                    fx_1 *= -1.0
                    if fx_1 < tolerance:
                        break
                    else:
                        fb = pn_1
                else:
                    if fx_1 < tolerance:
                        break
                    else:
                        fa_1 = pn_1
                iteration_1 += 1

            else:
                pn_1 = (fa_1 + fb) / 2
                fn_1 = evaluate(function=function, variable=variable, value=pn_1)
                fx_1 = evaluate(function=function, variable=variable, value=fa_1) * fn_1

                # iterations.append(
                # [fa_1, fb, ((fa_1 + fb) / 2), eval(function=function, variable=variable, value=pn_1)])
                # iterations['Iteration'].append(iteration_1)
                iterations['a_n'].append(fa_1)
                iterations['b_n'].append(fb)
                iterations['p_n'].append(((fa_1 + fb) / 2))
                iterations['f_n'].append(fn_1)
                if fx_1 < 0:
                    fx_1 *= -1.0
                    if fx_1 < tolerance:
                        break
                    else:
                        fb = pn_1
                else:
                    if fx_1 < tolerance:
                        break
                    else:
                        fa_1 = pn_1
                iteration_1 += 1

            if iteration_1 > limit:
                break
    data = DataFrame(iterations, columns=header)
    return data if not just_root else iterations["p_n"][iteration_1 - 1]


def secant(function, variable, intervals, tolerance=1e-10, limit=250, just_root=False):
    __configure__()
    iterations = {
        'x_n': [],
        'f(x_n)': []
    }
    header = ['x_n', 'f(x_n)']
    x_0 = 0.0
    x = 0.0
    n_iteration = 1
    while True:
        if n_iteration == 1:
            x_0 = intervals[0]
            x = intervals[1]
            fx_n_1 = evaluate(function, variable, x)
            fx_n = evaluate(function, variable, x_0)
            x_x_0 = x - x_0
            x_x = (x - fx_n_1 * x_x_0) / (fx_n_1 - fx_n)
            iterations['x_n'].append(x)
            iterations['f(x_n)'].append(fx_n)
            # iterations.append([n_iteration, x, x_0, fx_n])
            e_x = fx_n
            if e_x < 0:
                t_r = e_x * -1.0
                if t_r < tolerance:
                    break
                else:
                    x_0 = x
                    x = x_x
            else:
                if e_x < tolerance:
                    break
                else:
                    x_0 = x
                    x = x_x
            n_iteration += 1
        else:
            fx_n_1 = evaluate(function, variable, x)
            fx_n = evaluate(function, variable, x_0)
            x_x_0 = x - x_0
            if fx_n_1 - fx_n != 0:
                x_x = (x - fx_n_1 * x_x_0 / (fx_n_1 - fx_n))
            else:
                break
            iterations['x_n'].append(x)
            iterations['f(x_n)'].append(fx_n)
            # iterations.append([n_iteration, x, x_0, fx_n])
            e_x = fx_n
            if e_x < 0:
                t_r = e_x * -1.0
                if t_r < tolerance:
                    break
                else:
                    x_0 = x
                    x = x_x
            else:
                if e_x < tolerance:
                    break
                else:
                    x_0 = x
                    x = x_x
            n_iteration += 1
        if limit > 0:
            if n_iteration > limit:
                break
            elif n_iteration > 250:
                break
        elif n_iteration > 250:
            break
    data = DataFrame(iterations, columns=header)
    return data if not just_root else iterations['x_n'][len(iterations['x_n']) - 1]
