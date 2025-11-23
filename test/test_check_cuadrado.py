import pytest
from src.check_sudoku_cuadrado import check_cuadrado
import casosTest.casosTest as casosTest

@pytest.mark.es_cuadrado
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto_cuadrado_tresxtres, True)
        (casosTest.incorrecto_cuadrado_tresxtres, False),
        (casosTest.correcto_cuadrado_cuatroxcuatro, True),
        (casosTest.incorrecto_cuadrado_cuatroxcuatro, False),
    ],
)
def test_check_cuadrado(sudoku, sano):
    assert check_cuadrado(sudoku) == sano