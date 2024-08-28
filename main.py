linhas = int(input("Digite o número de linhas: "))

matriz = []

for linha in range(linhas):
    fila = []
    for coluna in range(linhas + 1):
        fila.append(int(input(f"[{linha + 1}][{coluna + 1}]: ")))
    matriz.append(fila)

for linha in matriz:
    print(linha)

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
