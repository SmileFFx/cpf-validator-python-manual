# Ler dois valores inteiros do usuário, repetindo enquanto a entrada for inválida
while True:
    try:
        valor1 = int(input("digite um valor: ").strip())
        break
    except ValueError:
        print("Valor inválido. Informe um número inteiro (ex: 5). Tente novamente.")

while True:
    try:
        valor2 = int(input("digite outro valor: ").strip())
        break
    except ValueError:
        print("Valor inválido. Informe um número inteiro (ex: 10). Tente novamente.")

# comparação de valores pra saber se um é maior que o outro

if valor1 > valor2:
    print(f"O valor {valor1} é maior que o valor {valor2}") 

elif valor2 > valor1:
    print(f"O valor {valor2} é maior que o valor {valor1}") 

else:
    print("Os valores são iguais")
    
# Ler dados do usuário (input retorna string)