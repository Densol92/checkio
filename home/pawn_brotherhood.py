# Пешка защищена, если её клетка находится по ударом другой своей пешки. На игровом поле находятся только белые пешки. Вы должны разработать код,
# позволяющий определить сколько пешек защищены в этой позиции.
# Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек.
# Входные данные: Координаты расставленных пешек в виде набора строк.
# Выходные данные: Количество защищенных пешек в виде целого числа.


def get_defended(cell):
    letter = ord(cell[0])
    previous_row = str(int(cell[1]) - 1)
    previos_letter, next_letter = letter - 1, letter + 1
    return {chr(previos_letter) + previous_row, chr(next_letter) + previous_row}


def safe_pawns(pawns):
    protected = 0
    for pawn in pawns:
        if len(get_defended(pawn) & set(pawns)) > 0:
            protected += 1
    return protected

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
