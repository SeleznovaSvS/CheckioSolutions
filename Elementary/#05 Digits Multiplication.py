def checkio(number: int) -> int:
    product = 10
    broj = 1
    auxiliary_list = [0, 1, 2, 3, 4, 5]
    auxiliary_var = 0
    for auxiliary_var in range(len(auxiliary_list)):
        if number % product == 0:
            broj *= 1
            number /= 10
        else:
            broj *= (number % product)
            number -= (number % product)
            number /= 10
    return int(broj)


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")