from datetime import date

# Ler dados do usuário
nome = input("Nome: ")
idade = int(input("Idade: "))
altura_metros = float(input("Altura (m): "))

# Calcular ano de nascimento a partir do ano atual
ano_nascimento = date.today().year - idade

# Booleano direto (True/False)
maior_idade = idade >= 18

print(
    f"Nome: {nome}\n"
    f"Idade: {idade}\n"
    f"Altura: {altura_metros:.2f}m\n"
    f"Ano de nascimento: {ano_nascimento}\n"
    f"Maior de idade: {maior_idade}"
)