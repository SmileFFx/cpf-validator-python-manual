# ============================================
# EXERCÍCIOS SOBRE TRY / EXCEPT
# ============================================

# 1️⃣
# Peça ao usuário um número e mostre o dobro dele.
# Use try/except para capturar erros caso o usuário digite algo que não seja número.

# Exemplo esperado:
# Digite um número: abc
# Saída: Valor inválido! Por favor, digite um número.
# while True:
#     entrada = input("Digite um número: ").strip()
#     try:
#         numero = float(entrada)          # tenta converter para float
#         break                           # ok: sai do loop
#     except ValueError:
#         print("Valor inválido! Por favor, digite um número.")

# # agora 'numero' é um float válido
# dobro = numero * 2
# print(f"O dobro de {numero} é {dobro}.")

# fim do codigo

# 2️⃣
# Peça dois números ao usuário e tente dividir o primeiro pelo segundo.
# Use try/except para evitar erro de divisão por zero e erro de tipo (str, etc).

# while True:
#     try:
#         num1 = float(input("Digite o primeiro número: ").strip())
#         num2 = float(input("Digite o segundo número: ").strip())
#         break
#     except ValueError:
#         print("Erro! Por favor, digite números válidos.")

# try:
#     resultado = num1 / num2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro! Não é possível dividir por zero.")

# fim do codigo




# Exemplo esperado:teste
# Digite o primeiro número: 10
# Digite o segundo número: 0
# Saída: Erro! Não é possível dividir por zero.


# 3️⃣
# Crie uma função chamada 'abrir_arquivo' que tenta abrir um arquivo "dados.txt".
# Se o arquivo não existir, capture a exceção e exiba uma mensagem de erro amigável.
# (Dica: use `open("dados.txt")` dentro de try/except)

# def abrir_arquivo():
#     try:
#         arquivo = open("dados.txt")
#         conteudo = arquivo.read()
#         print(conteudo)
#         arquivo.close()
#     except FileNotFoundError:
#         print("O arquivo 'dados.txt' não foi encontrado.")
# # Chama a função para testar
# abrir_arquivo()




# 4️⃣
# Crie um programa que peça um número inteiro e converta-o para int dentro de um try.
# Se falhar, mostre "Entrada inválida!" e peça novamente até conseguir um número válido.
# (Dica: use while True com break quando der certo)

# while True:
#     try:
#         numero = int(input("Digite um número inteiro: ").strip())
#         print(f"Você digitou um valor valido")
#         break
#     except ValueError:
#         print("Entrada inválida")
              


# ============================================
# EXERCÍCIOS SOBRE WHILE
# ============================================

# 5️⃣
# Use um loop while para imprimir os números de 1 a 10.

# n = 0
# while n < 10:
#     n += 1
#     print(n)



# 6️⃣
# Peça ao usuário para digitar "sair" para encerrar o programa.
# Enquanto ele não digitar "sair", continue pedindo um novo texto.
# while True:
#     try:
#         # <pede ao usuário que digite algo e remove espaços extras>
#         texto = input("Digite 'sair' para encerrar o programa: ").strip().lower()

#         # <verifica se o usuário digitou 'sair'>
#         if texto == "sair":
#             print("Programa encerrado.")
#             break  # <interrompe o loop>
#         else:
#             # <caso não tenha digitado 'sair', mostra uma mensagem>
#             print("Digite 'sair' para encerrar o programa.")

#     # <captura qualquer erro que possa ocorrer dentro do bloco try>
#     except Exception as e:
#         # <exibe o erro ocorrido>
#         print(f"Ocorreu um erro: {e}")


# 7️⃣
# Peça ao usuário números até que ele digite 0.
# Ao final, mostre a soma de todos os números digitados (exceto o 0).
"pulado"



# 8️⃣
# Use um while para simular um contador de tentativas.
# O usuário tem até 3 tentativas para adivinhar um número secreto (por exemplo, 7).
# Se acertar, mostre "Acertou!" e pare o loop.
# Se errar 3 vezes, mostre "Fim das tentativas!".
# # import random
# # secreto = random.randint(1,10)                            # número secreto
# # max_tentativas = 3                  # máximo de tentativas
# # tentativas = 0                          # contador de tentativas

# # while tentativas < max_tentativas:
# #     try:
# #         palpite = int(input("Adivinhe o número secreto (de 1 a 10): ").strip())
# #         tentativas += 1
# #         if palpite == secreto:
# #             print("Acertou!")
# #             break
# #         else:
# #             print(f"Errado ! vocÊ tem mais {max_tentativas - tentativas} tentativas.")
# #     except ValueError:
# #         print("Digite apenas números inteiros de 1 a 10.")

# # if tentativas == max_tentativas:
# #     print("Fim das tentativas! O número secreto era:", secreto)

    #FIM DO CODIGO
# 9️⃣
# Crie um menu simples com while:
# 1 - Somar dois números
# 2 - Subtrair dois números
# 3 - Sair
# Use try/except para garantir que as entradas são números válidos.
# while True:
#     print("Menu:\n"
#           "1 - Somar dois números\n"
#           "2 - Subtrair dois números\n"
#           "3 - Sair")
          
#     escolha = input("Escolha uma opção (1, 2 ou 3): ").strip()
    
#     if escolha == "1":
#         try:
#             # <peça os números aqui, somente se a opção for soma>
#             n1_1 = int(input("Digite o primeiro número da soma: "))
#             n1_2 = int(input("Digite o segundo número da soma: "))
#             resultado_soma = n1_1 + n1_2
#             print(f"O resultado da soma é: {resultado_soma}")
#         except ValueError:
#             print("Entrada inválida! Por favor, digite números válidos.")

#     elif escolha == "2":
#         try:
#             # <peça os números aqui, somente se a opção for subtração>
#             n2_1 = int(input("Digite o primeiro número da subtração: "))
#             n2_2 = int(input("Digite o segundo número da subtração: "))
#             resultado_subtracao = n2_1 - n2_2
#             print(f"O resultado da subtração é: {resultado_subtracao}")
#         except ValueError:
#             print("Entrada inválida! Por favor, digite números válidos.")

#     elif escolha == "3":
#         print("Saindo do programa. Até mais!")
#         break

#     else:
#         print("Opção inválida! Por favor, escolha 1, 2 ou 3.")


          
          
          

# 🔟
# Combine while + try/except:
# Peça um número e divida 100 por ele.
# Continue pedindo até que o usuário digite um número válido e diferente de zero.
