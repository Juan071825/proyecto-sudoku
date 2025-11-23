def check_repetición_columna(sudoku):
    contador_columna = 0
    UNO = 1

    while contador_columna < len(sudoku):
        columna = []
        
        for fila in sudoku:
            columna.append(fila[contador_columna]) # aquí en vez de sudoku debería poner fila y cargarme contador_fila.
        contador_columna += UNO

        for numero in columna:
            if columna.count(numero) > UNO:
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
            print(attr, "=>", check_repetición_columna(casosTest.__dict__[attr]))
    