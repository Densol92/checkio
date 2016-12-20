def checkio(number):
    ones = 0
    binary = bin(number)
    for c in binary:
        if c == '1':
            ones += 1
    return ones

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
