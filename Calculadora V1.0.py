def calculate():
    operation = input('''
    Por favor, escolha uma das operações:
    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    ''')

    number_1 = int(input('Primeiro número: '))
    number_2 = int(input('Segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você digitou uma operação inválida, por favor, reinicie o programa.')
        
def again():
    calc_again = input('''
    Quer calcular denovo ?
    SIM ou NAO ?
    ''')

    if calc_again.upper() == 'SIM':
        calculate()
    elif calc_again.upper() == 'NAO':
        print('Tchau!')
    else:
        again()

calculate()
