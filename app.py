from src.sudoku import check_sudoku
import casosTest.casosTest as casosTest

for attr in sorted(casosTest.__dict__):

    if attr.startswith('__'):
        pass
    else:
        print(attr, "=>", check_sudoku(casosTest.__dict__[attr]))