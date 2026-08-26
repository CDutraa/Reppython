# input da operação
operacao = input('Será uma soma, subtração, divisão ou multiplicação?: ')
operacao = operacao.lower().strip()

# listas das operações
soma = ['soma']
sub = ['subtração', 'subtraçao', 'subtracão', 'subtracao']
div = ['divisão', 'divisao']
multi = ['multiplicação', 'multiplicaçao', 'multiplicacão', 'multiplicacao']

# while para enquanto o usuario digitar errado
while operacao not in soma and operacao not in sub and operacao not in div and operacao not in multi:
    print('Essa operação não existe ou está escrita incorretamente!')

    operacao = input('Será uma soma, subtração, divisão ou multiplicação?: ')
    operacao = operacao.lower().strip()

# input dos numeros para a conta
n1 = float(input('numero 1: '))
n2 = float(input('numero 2: '))

# SOMA
if operacao in soma:
    resultado = n1 + n2
    print(f'O resultado da sua soma é: {resultado:g}')

# SUBTRAÇÃO
elif operacao in sub:
    resultado = n1 - n2 
    print(f'O resultado da sua subtração é: {resultado:g}')

# DIVISÃO
elif operacao in div:
    if n2 == 0:
        print('Erro: Não é possível dividir por zero.')
    else:  
        resultado = n1 / n2
        print(f'O resultado da sua divisão é: {resultado:g}')

# MULTIPLICAÇÃO
elif operacao in multi:
    resultado = n1 * n2
    print(f'O resultado da sua multiplicação é: {resultado:g}')

print("alteraçao")