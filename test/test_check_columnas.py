import pytest
from src.check_repetición_columna import check_repetición_columna
import casosTest.casosTest as casosTest

@pytest.mark.columnas_validas
@pytest.mark.parametrize(
    "sudoku, sano",
    [

(casosTest.correcto_repetición_columna_tresxtres, True),
(casosTest.incorrecto_repetición_columna_tresxtres, False),
(casosTest.correcto_repetición_columna_cuatroxcuatro, True),
(casosTest.incorrecto_repetición_columna_cuatroxcuatro, False),
    ],
)
def test_check_columnas(sudoku, sano):
    assert check_repetición_columna(sudoku) == sano

