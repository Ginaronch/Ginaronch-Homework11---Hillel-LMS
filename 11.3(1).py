def is_even(number):
    number = str(number)
    if number.endswith("2") == True:
        return True
    elif number.endswith("4") == True:
        return True
    elif number.endswith("6") == True:
        return True
    elif number.endswith("8") == True:
        return True
    elif number.endswith("0") == True:
        return True
    else:
        return False
assert is_even(2494563894038**2) == True
assert is_even(1056897**2) == False
assert is_even(24945638940387**3) == False
print("OK")