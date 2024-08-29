linhas = int(input("Digite o número de linhas: ")) # Usuário define o número de linhas

matriz = []

# Alimentação da matriz:
for linha in range(linhas):
    fila = [] # Cria uma linha que será inserida na matriz ao final do loop
    for coluna in range(linhas + 1):
        fila.append(int(input(f"[{linha + 1}][{coluna + 1}]: "))) # Adicona valores digitados pelo usuário à linha
    matriz.append(fila) # Adiciona cada linha à matriz

for linha in matriz:
    print(linha) # Imprime a matriz informada pelo usuário

# Bloco de escalonamento:
i = 0
while i < len(matriz):
    j = 0
    pivo = matriz[i][i] # Pivô sempre é o elemento em que i = j
    # Loop para transformar primeiro elemento não nulo em 1
    for elemento in matriz[i]:
        matriz[i][j] *= 1 / pivo # Essa operação faz com que primeiro elemento não nulo de cada linha seja transformado em 1
        j += 1
    
    # Bloco para zerar elementos da coluna do pivô
    i_pivo = 0
    j_pivo = i
    while i_pivo < len(matriz):
        if matriz[i_pivo][j_pivo] != 0 and i_pivo != i:
            pivo = -matriz[i_pivo][j_pivo]
            linha_temp = [] # Essa lista é necessária para que os elementos de uma linha sejam multiplicados pelo oposto do pivô sem que a matriz seja alterada
            for elemento in matriz[i]:
                elemento *= pivo # Operação para zerar elementos da coluna do pivô
                linha_temp.append(elemento)
            for indice, elemento in enumerate(matriz[i_pivo]):
                matriz[i_pivo][indice] += linha_temp[indice]
        i_pivo += 1
    i += 1

for linha in matriz:
    print(linha) # Imprime a matriz escalonada
