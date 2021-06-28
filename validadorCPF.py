while True:
    cpf = input('Digite um CPF (somente números): ').strip()
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

    if cpf == novoCpf:
        print('Válido')
    else:
        print('Inválido')

    continuar = input('Deseja validar outro CPF? [S/N] ').strip().upper()
    if continuar == 'S':
        continue
    else:
        quit()