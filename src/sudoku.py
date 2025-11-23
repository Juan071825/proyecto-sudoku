import sys

sys.path.append("..")

from check_sudoku_nulo import check_sudoku_nulo
from check_sudoku_cuadrado import check_cuadrado
from check_numeros_validos import check_numeros_validos
from check_repetición_fila import check_repetición_fila
from check_repetición_columna import check_repetición_columna

def check_sudoku(sudoku):
    return (
        check_sudoku_nulo(sudoku)
        and check_cuadrado(sudoku)
        and check_numeros_validos(sudoku)
        and check_repetición_fila(sudoku)
        and check_repetición_columna(sudoku)
    )


if __name__ == "__main__":
    print("Estamos en el main de sudoku.py")

    import sys

    sys.path.append("..")

    import casosTest.casosTest as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, "=>", check_sudoku(casosTest.__dict__[attr]))

