import pytest
from src.check_numeros_validos import check_numeros_validos
import casosTest.casosTest as casosTest


@pytest.mark.numeros_validos
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto_numeros_tresxtres, True),
        (casosTest.incorrecto_numeros_tresxtres, False),
        (casosTest.correcto_numeros_cuatroxcuatro, True),
        (casosTest.incorrecto_numeros_cuatroxcuatro, False),
    ],
)
def test_check_numeros_validos(sudoku, sano):
    assert check_numeros_validos(sudoku) == sano