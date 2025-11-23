incorrecto_sudoku_nulo = []
correcto_sudoku_lleno = [[1, 2, 3]]
# /--------------------------------------------------------/
incorrecto_cuadrado_tresxtres = [[1,2,3],
                                 [2,1, ],
                                 [3,3,2]]

correcto_cuadrado_tresxtres = [[1, 2, 3],
                               [3, 1, 2],
                               [2, 3, 1]]
incorrecto_cuadrado_cuatroxcuatro = [[1, 2, 3, 4],
                                     [2, 1, 3, 1],
                                     [3, 3, 2, 2]]

correcto_cuadrado_cuatroxcuatro = [[1, 2, 3, 4],
                                   [4, 1, 2, 3],
                                   [2, 3, 1, 4],
                                   [1, 2, 3, 4]]
# /--------------------------------------------------------------/
incorrecto_numeros_tresxtres =  [[1, 2, 3],
                                 [2, 0, 3],
                                 [3, 3, 2]]

correcto_numeros_tresxtres =  [[1, 2, 3],
                               [3, 1, 2],
                               [2, 3, 1]]
incorrecto_numeros_cuatroxcuatro =  [[1, 2, 3, 4],
                                     [2, 1, 3, 1],
                                     [3, 3, 5, 2],
                                     [1, 2, 3, 4]]

correcto_numeros_cuatroxcuatro =  [[1, 2, 3, 4],
                                   [4, 1, 2, 3],
                                   [2, 3, 1, 4],
                                   [1, 2, 3, 4]]

# /----------------------------------------------------------------------/
incorrecto_repetición_fila_tresxtres =  [[1, 2, 3],
                                         [2, 1, 3],
                                         [3, 1, 1]]

correcto_repetición_fila_tresxtres =  [[1, 2, 3],
                                       [3, 1, 2],
                                       [2, 3, 1]]
incorrecto_repetición_fila_cuatroxcuatro =  [[1, 2, 3, 4],
                                          [2, 1, 3, 1],
                                          [3, 3, 5, 2],
                                          [1, 2, 3, 4]]

correcto_repetición_fila_cuatroxcuatro =  [[1, 2, 3, 4],
                                        [4, 1, 2, 3],
                                        [2, 3, 1, 4],
                                        [1, 2, 3, 4]]

# /----------------------------------------------------------------------------/
incorrecto_repetición_columna_tresxtres =  [[1, 2, 3],
                                            [2, 1, 3],
                                            [3, 1, 1]]

correcto_repetición_columna_tresxtres =  [[1, 2, 3],
                                          [3, 1, 2],
                                          [2, 3, 1]]
incorrecto_repetición_columna_cuatroxcuatro =  [[1, 2, 3, 4],
                                             [2, 1, 3, 1],
                                             [3, 3, 5, 2],
                                             [1, 2, 3, 4]]

correcto_repetición_columna_cuatroxcuatro =  [[1, 4, 3, 2],
                                           [2, 3, 2, 4],
                                           [3, 2, 1, 1],
                                           [4, 1, 4, 3]]