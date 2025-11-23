import pytest
from src.check_repetición_fila import check_repetición_fila
import casosTest.casosTest as casosTest


@pytest.mark.filas_validas
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto_repetición_fila_tresxtres, True),
        (casosTest.incorrecto_repetición_fila_tresxtres, False),
        (casosTest.correcto_repetición_fila_cuatroxcuatro, True),
        (casosTest.incorrecto_repetición_fila_cuatroxcuatro, False),
    ],
)
def test_check_filas(sudoku, sano):
    assert check_repetición_fila(sudoku) == sano