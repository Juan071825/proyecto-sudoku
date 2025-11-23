def check_sudoku_nulo(sudoku):
    if not sudoku:
        return False
    return True



if __name__ == '__main__':
    import sys
    sys.path.append("..")
    import casosTest.casosTest as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        
        else:
            print(attr, "=>", check_sudoku_nulo(casosTest.__dict__[attr]))
    