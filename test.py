import nupy as nup

iterations = nup.intermediate_value(function="x**3-5", variable="x", intervals=[1, 2], tolerance=1e-50, limit=0)
print(iterations)
