from nupy.iterate import intermediate_value, secant

iterations_2 = secant(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True)
print(iterations_2)

iterations_2 = secant(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60)
print(iterations_2.head(15))

iterations = intermediate_value(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60, just_root=True)
print(iterations)

iterations = intermediate_value(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-60)
print(iterations.head(15))
