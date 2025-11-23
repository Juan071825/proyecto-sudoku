def check_cuadrado(sudoku):
    #contador_fila = 0 #el contador sería necesario con un while
    UNO = 1
    
    for fila in sudoku:
        if len(sudoku) != len(fila): #(sudoku[contador_fila]): no hace falta el contador, for fila in sodoku ya recorre las filas.
            return False
        #contador_fila += UNO
    return True




if __name__ == '__main__':
    import sys
    sys.path.append("..")
    import casosTest.casosTest as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        
        else:
            print(attr, "=>", check_cuadrado(casosTest.__dict__[attr]))
    