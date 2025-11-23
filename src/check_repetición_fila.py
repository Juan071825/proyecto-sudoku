def check_repetición_fila(sudoku):
    #contador_filas = 0
    UNO = 1

    for fila in sudoku:
        for numero in fila:
            if fila.count(numero) > UNO:
                return False
            #contador_filas += UNO tampoco hace falta
    return True




if __name__ == '__main__':
    import sys
    sys.path.append("..")
    import casosTest.casosTest as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        
        else:
            print(attr, "=>", check_repetición_fila(casosTest.__dict__[attr]))
    