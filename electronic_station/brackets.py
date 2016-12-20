def checkio(expression):
    mapa = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    stack = []
    is_correct = True
    for symbol in expression:
        if symbol in mapa.values():
            stack.append(symbol)
        elif symbol in mapa.keys():
            if len(stack) > 0 and stack[-1] == mapa[symbol]:
                stack.pop()
            else:
                is_correct = False
    if stack:
        is_correct = False
    return is_correct


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((1+(1+1))))]") == False