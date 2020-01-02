def checkio(data: str) -> bool:
    # replace this for solution
    # Checking Length
    length = len(data)
    if (length < 10):
        return False

    # Checking characters
    digit = False
    upper = False
    lower = False
    i = 0
    while (i < length and (not (digit) or not (upper) or not (lower))):
        char = data[i]
        if (char.isupper()):
            upper = True
        elif (char.isdigit()):
            digit = True
        elif (char.islower()):
            lower = True
        i += 1
    return (digit and upper and lower)


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
