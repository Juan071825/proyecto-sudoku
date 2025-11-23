import pytest
from src.check_sudoku_nulo import check_sudoku_nulo
import casosTest.casosTest as casosTest

@pytest.mark.sudoku_lleno
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto_sudoku_lleno, True),
        (casosTest.incorrecto_sudoku_nulo, False),
    ],
)
def test_check_sudoku_nulo(sudoku, sano):
    assert check_sudoku_nulo(sudoku) == sano