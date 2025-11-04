# calculadora com while
while True:
    n1 = input("digite um numero:  ")
    n2 = input("digite outro numero:  ")
    operador = input("digite o operador (+, -, *, /): ")

    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        print("Por favor, digite números válidos.")
        continue

    if operador == "+":
        resultado = n1 + n2
    elif operador == "-":
        resultado = n1 - n2
    elif operador == "*":
        resultado = n1 * n2
    elif operador == "/":
        if n2 == 0:
            print("Erro: Divisão por zero não é permitida.")
            continue
        resultado = n1 / n2
    else:
        print("Operador inválido. Tente novamente.")
        continue

    print(f"O resultado de {n1} {operador} {n2} é: {resultado}")
    
    while True:
        sair = input("Deseja sair? (s/n): ").strip().lower()
        if sair in ('s', 'n'):
            break
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    if sair == 's':
        break

# fim do programa


