def generate_cube_numbers(end):
    for number in range(2, end):
        cube = number ** 3
        if cube > end:
            break
        yield cube
from inspect import isgenerator
gen = generate_cube_numbers(1)
assert isgenerator(gen) == True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("OK")