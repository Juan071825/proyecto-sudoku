import pytest
from src.sudoku import check_sudoku
import casosTest.casosTest as casosTest


@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto_sudoku_lleno, True),
        (casosTest.incorrecto_sudoku_nulo, False),
        (casosTest.correcto_cuadrado_tresxtres, True)
        (casosTest.incorrecto_cuadrado_tresxtres, False),
        (casosTest.correcto_cuadrado_cuatroxcuatro, True),
        (casosTest.incorrecto_cuadrado_cuatroxcuatro, False),
        (casosTest.correcto_numeros_tresxtres, True),
        (casosTest.incorrecto_numeros_tresxtres, False),
        (casosTest.correcto_numeros_cuatroxcuatro, True),
        (casosTest.incorrecto_numeros_cuatroxcuatro, False),
        (casosTest.correcto_repetición_fila_tresxtres, True),
        (casosTest.incorrecto_repetición_fila_tresxtres, False),
        (casosTest.correcto_repetición_fila_cuatroxcuatro, True),
        (casosTest.incorrecto_repetición_fila_cuatroxcuatro, False),
        (casosTest.correcto_repetición_columna_tresxtres, True),
        (casosTest.incorrecto_repetición_columna_tresxtres, False),
        (casosTest.correcto_repetición_columna_cuatroxcuatro, True),
        (casosTest.incorrecto_repetición_columna_cuatroxcuatro, False),

    ],
)
def check_sudoku(sudoku, sano):
    assert check_sudoku(sudoku) == sano