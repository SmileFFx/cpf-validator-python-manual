# Faça um jogo para o usuário adivinhar qual
# a palavra secreta.
# - Você vai propor uma palavra secreta
# qualquer e vai dar a possibilidade para
# o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você 
# vai conferir se a letra digitada está
# na palavra secreta.
#     - Se a letra digitada estiver na
#     palavra secreta; exiba a letra;
#     - Se a letra digitada não estiver
#     na palavra secreta; exiba *.
# Faça a contagem de tentativas do seu
# usuário.
# """
pl_se = "Akashi".lower()      #palavra secreta
tentativas = 0                #contador de tentativas
letras_acertadas = []         #lista para armazenar letras acertadas

#  isso transforma cada letra da palavra secreta em um asterisco
for letra in pl_se:
    letras_acertadas.append("*")

#demonstração se a letra foi ou não acertada

while True:
    letra_user = input("digite uma letra: ").lower()
    tentativas += 1
    if len(letra_user) != 1 or not letra_user.isalpha():   #se a quantidade de letras digitadas for diferente de 1 ou não for uma letra do alfabeto
        print("Por favor, digite apenas uma letra válida.") #retorna essa mensagem
        continue
    acertou = False
    for index, letra in enumerate(pl_se):                  #verificia se a letra digitada está na palavra secreta
        if letra_user == letra:
            letras_acertadas[index] = letra_user
            acertou = True
    if not acertou:                                        #se a letra não foi acertada 
        print(" ".join(letras_acertadas))
    else:
        print(" ".join(letras_acertadas))
    if "*" not in letras_acertadas:
        print(f"Parabéns! Você acertou a palavra '{pl_se}' em {tentativas} tentativas.")
        break                                                  #ao final se acertar toda a palavra, o loop é interrompido
# fim do codigo