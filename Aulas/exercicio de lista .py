# faça uma lista de comprar com listas.
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com erros de índices inexistentes na lista.
# """


import os
lista_de_compras = []

while True:
    print('Escolha uma opção:')
    input_usuario = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    # aqui o usuario escolhe a ação que deseja fazer
    if input_usuario == 'i':
        os.system('cls')
        item = input('Digite o item que deseja inserir: ')
        lista_de_compras.append(item)
    # insere o item na lista

    elif input_usuario == 'a':
        os.system('cls')
        print('Lista de compras:')
        for indice, item in enumerate(lista_de_compras):
            print(f'{indice}: {item}')
        try:
            indice = int(input('Digite o índice do item que deseja apagar: '))
            lista_de_compras.pop(indice)
        except (ValueError, IndexError):
            print('Índice inválido. Tente novamente.')
    # apaga o item da lista conforme o índice digitado pelo usuário

    elif input_usuario == 'l':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('A lista de compras está vazia.')
            continue
        print('Lista de compras:')
        for indice, item in enumerate(lista_de_compras):
            print(f'{indice}: {item}')
    # lista os itens da lista de compras

    elif input_usuario == 's':
        os.system('cls')
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida. Tente novamente.')