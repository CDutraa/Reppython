# input dos numeros e operação
print("\nDigite os números que deseja calcular\n")
n1 = float(input('numero 1: '))
n2 = float(input('numero 2: '))
op = input("Digite o tipo de operação (+, -, /, *): ")

#switch-case do python
def calcular(n1, n2, op):
    match op:
        case '+':
            resultado = n1 + n2
            print(f'O resultado da sua soma é: {resultado:g}')
        case '-':
            resultado = n1 - n2
            print(f'O resultado da sua subtração é: {resultado:g}')
        case '/':
            try:
                resultado = n1 / n2
                print(f'O resultado da sua divisão é: {resultado:g}')
            except ZeroDivisionError:
                print("Erro! Não é possível dividir por zero")
        case '*':
            resultado = n1 * n2
            print(f'O resultado da sua multiplicação é: {resultado:g}')

#enquanto a operação nao for valida, ele vai pedir para digitar novamente
while op not in ['+', '-', '*', '/']:
    print('Erro: Operação inválida!\nPor favor, digite uma operação válida (+, -, *, /).')
    op = input("Digite o tipo de operação (+, -, /, *): ")
else:
    calcular(n1, n2, op)


