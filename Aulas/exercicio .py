# nome = input("digite seu nome:")
# idade = input("digite sua idade:")
# if nome and idade :
#     print( f"olá {nome} você tem {idade} anos\n"
#            f"a primeira letra do seu nome é {nome[0]}\n"
#            f"o seu nome tem {len(nome)} letras\n"
#            f"o seu nome detras para frente é {nome[::-1]}\n"
#            f"seu nome contem {nome.count(' ')} espaços\n"
#            f"a ultima letra do seu nome é {nome[-1]}\n"
#     )
# else:
#     print("você não digitou nada!")

# @@ -0,0 +1,17 @@
# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """
while True:
    entrada = input("Digite um número inteiro: ").strip()
    try:
        entrada = int(entrada)                # tenta converter para inteiro
        break                              # ok: sai do loop
    except ValueError:
        print("Isso não é um número inteiro. Tente novamente.")

# agora 'entrada' é um int válido
if entrada % 2 == 0:
    print(f"O número {entrada} é par.")
else:
    print(f"O número {entrada} é ímpar.")



# """
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
while True:
    hora = input ("Que horas são? ").strip()
    try:
        hora = int(hora)              # tenta converter para inteiro
        if hora < 0 or hora > 23:
            print("Hora inválida. Digite um valor entre 0 e 23.")
            continue
        break                          # ok: sai do loop
    except ValueError:
        print("Isso não é uma hora válida. Tente novamente.")

# agora 'hora' é um int válido entre 0 e 23
if hora >= 0 and hora <=11:
    print("Bom dia!")

elif hora >=12 and hora <=17:
    print("Boa tarde!") 

else:
    print("Boa noite!")

    # fim do codigo 

# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """
while True:
    nome = input("digite seu nome: ").strip()
    try:
        nome = str(nome)              # tenta converter para string
        break                               # ok: sai do loop 
    except ValueError:
        print("Isso não é um nome válido. Tente novamente.")

# agora 'nome' é uma string válida

tamanho = len(nome)
if tamanho <= 4:
    print("Seu nome é curto")
elif tamanho >= 5 and tamanho <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")

    # fim do codigo
