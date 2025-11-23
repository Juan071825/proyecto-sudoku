def check_numeros_validos(sudoku):
    #contador_filas = 0
    UNO = 1
    for fila in sudoku:
        for numero in fila:
            if numero not in range(UNO,len(sudoku) + UNO):
                return False
        #contador_filas += UNO #tampoco hace falta el contador_filas
    return True
    




if __name__ == '__main__':
    import sys
    sys.path.append("..")
    import casosTest.casosTest as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        
        else:
            print(attr, "=>", check_numeros_validos(casosTest.__dict__[attr]))
    
    
   