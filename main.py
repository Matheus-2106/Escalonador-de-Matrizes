matriz = [[2, 1, 1, 1, 1],
          [1, 2, 1, 1, 2],
          [1, 1, 2, 1, 3],
          [1, 1, 1, 2, 4]]

i = 0

while i < len(matriz):
    j = 0
    pivo = matriz[i][i]
    for elemento in matriz[i]:
        matriz[i][j] *= 1 / pivo
        j += 1
    
    i_pivo = 0
    j_pivo = i
    while i_pivo < len(matriz):
        if matriz[i_pivo][j_pivo] != 0 and i_pivo != i:
            pivo = -matriz[i_pivo][j_pivo]
            linha_temp = []
            for elemento in matriz[i]:
                elemento *= pivo
                linha_temp.append(elemento)
            for indice, elemento in enumerate(matriz[i_pivo]):
                matriz[i_pivo][indice] += linha_temp[indice]
        i_pivo += 1

    i += 1

for linha in matriz:
    print(linha)
                                                          