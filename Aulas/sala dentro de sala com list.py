
def calculadora():
    while True:
        expressao = input("Digite uma conta (ou 'sair' para encerrar): ")

        if expressao.lower() == "sair":
            print("Encerrando...")
            break

        try:
            # verifica se é o código secreto
            if expressao.replace(" ", "") == "977+10":
                print("Espaço secreto desbloqueado!\n")
                # aqui poderia ter um novo menu, jogo, etc.
                continue

            # calcula a expressão normalmente
            resultado = eval(expressao)
            print(f"Resultado: {resultado}\n")

        except Exception as e:
            print("Expressão inválida, tente novamente.\n")

# executa
calculadora()