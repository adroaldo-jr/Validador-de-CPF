while True:
    cpf = input('Digite um CPF (somente números): ').strip()
    
    # Faz os cálculos para validar o CPF
    novoCpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        
        total += int(novoCpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0
            total = 0
            novoCpf += str(digito)

    # Verifica se o cpf inserido não é apenas sequência de um único número
    sequencia = novoCpf == str(novoCpf[0]) * len(cpf)

    # Verifica se o resultado é válido ou inválido
    if cpf == novoCpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')

    # Verifica se o programa deve continuar rodando
    continuar = input('Deseja validar outro CPF? [S/N] ').strip().upper()
    try:
        if continuar == 'S':
            continue
        else:
            quit()
    except:
        while continuar not in 'SN':
            continuar = input('Deseja validar outro CPF? [S/N] ').strip().upper()
        if continuar == 'S':
            continue
        else:
            quit()