frase = (
    "python é uma linguagem multiparadigma "
    "python foi criado por guido van rossum."
).lower()

print(frase)

# Pergunta ao usuário qual letra contar e valida a entrada
while True:

    letra = input("Qual letra deseja contar quantas vezes ela aparece na frase acima? ").strip().lower()
    if len(letra) == 1 and letra.isalpha():
        break
    print("Por favor digite apenas UMA letra (a-z). Tente novamente.")

quantidade = frase.count(letra)
print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")
