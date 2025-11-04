cpf = input("Digite o CPF (somente dígitos): ")    # cpf fornecido pelo usuário (apenas para fins acadêmicos)
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0 
#aqui se inicia o calculo do primeiro digito
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1      
digito_1 = (resultado * 10) % 11   
digito_1 = digito_1 if digito_1 <= 9 else 0   


#agora o segundo digito 
dez_digitos = nove_digitos + str(digito_1) 
contador_regressivo = 11       
resultado = 0

#aqui se inicia o calculo do segundo digito
for digito in dez_digitos:
    resultado +=int(digito) * contador_regressivo  
    contador_regressivo -= 1                       
digito_2 = (resultado * 10) % 11                  
digito_2 = digito_2 if digito_2 <= 9 else 0        

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}' #juntando tudo para formar o cpf completo
print(cpf_gerado)

if cpf == cpf_gerado:        #verificando se o cpf gerado é igual ao cpf inicial
    print('CPF Válido')
else:
    print('CPF Inválido')
#fim do código 
