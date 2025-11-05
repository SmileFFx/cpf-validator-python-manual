def ler_numero(mensagem):
    """Pede um número e valida até o usuário digitar um valor float válido."""
    while True:
        valor = input(mensagem)
        try:
            return float(valor)
        except ValueError:
            print("❌ Valor inválido. Digite um número válido (ex: 10 ou 3.5).")

while True:
    n1 = ler_numero("Digite um número: ")
    n2 = ler_numero("Digite outro número: ")

    while True:  # loop apenas para o operador
        operador = input("Digite o operador (+, -, *, /): ").strip()

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
            continue  # volta a pedir o operador

        # só chega aqui se o operador for válido
        break

    print(f"O resultado de {n1} {operador} {n2} é = {resultado}")

    while True:
        sair = input("Deseja sair? (s/n): ").strip().lower()
        if sair in ('s', 'n'):
            break
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")

    if sair == 's':
        break

print("Programa encerrado.")