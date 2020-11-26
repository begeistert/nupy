from nupy.iterative_methods import intermediate_value, secant


def roots():
    iterations_2 = secant(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True)
    iterations = intermediate_value(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True)
    return [iterations, iterations_2]


# iterations_2 = secant(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60)
# print(iterations_2.head(15))

# iterations = intermediate_value(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60)
# print(iterations.head(15))

def test_answer():
    for i in roots():
        assert i == 1.709975946676697
