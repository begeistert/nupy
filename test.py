from nupy.iterative_methods import intermediate_value, secant, fixedPoint, falsePosition


def roots():
    return [secant(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True),
            intermediate_value(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True),
            fixedPoint(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True),
            falsePosition(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True)]


def test_answer():
    for i in roots():
        assert i == 1.709975946676697
