def calculate():
    operation = input('''
    Calculadora do Matilha San:
    
    Por favor, escolha uma das operações e digite o simbolo dela, ou o nome e depois aperte ENTER:
    
    + adição
    
    - subtração
    
    * multiplicação
    
    / divisão

    Para reiniciar o programa, digite denovo().
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

    elif operation == 'adição':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == 'subtração':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == 'multiplicação':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == 'divisão':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você digitou uma operação inválida, por favor, reinicie o programa digitando denovo().')
        
def denovo():
    calc_denovo = input('''
    Quer calcular denovo ?
    SIM ou NAO ?
    ''')

    if calc_denovo.upper() == 'SIM':
        calculate()
    elif calc_denovo.upper() == 'NAO':
        print('Tchau!')
    elif calc_denovo.upper() == 'sim':
        calculate()
    elif calc_denovo.upper() == 'não':
        print('Tchau!')
    elif calc_denovo.upper() == 'nao':
        print('Tchau!')
    elif calc_denovo.upper() == 'Sim':
        calculate()
    elif calc_denovo.upper() == 'Nao':
        print('Tchau!')
    elif calc_denovo.upper() == 'Não':
        print('Tchau!')
    else:
        denovo()

calculate()
#ainda trabalhando em mais atualizações
