def calculate():
    operation = input('''
    Calculadora do Killian San aka Matilha San V3.1
    
    Por favor, escolha uma das operações e digite o simbolo dela ou o nome e depois aperte ENTER:
    
    + adição | 3+ adição de 3 números | 4+ adição de 4 números
    
    - subtração | 3- subtração de 3 números | 4- subtração de 4 números
    
    * multiplicação | 3* multiplicação de 3 números | 4* multiplicação de 4 números
    
    / divisão | 3/ divisão de 3 números | 4/ divisão de 4 números

        Para reiniciar o programa, digite denovo().
    ''')

    number_1 = int(input('Primeiro Número: '))
    number_2 = int(input('Segundo Número: '))
    if operation == '3+':
        number_3 = int(input('Terceiro Número: '))
    if operation == '3-':
        number_3 = int(input('Terceiro Número: '))
    if operation == '3*':
        number_3 = int(input('Terceiro Número: '))
    if operation == '3/':
        number_3 = int(input('Terceiro Número: '))
    if operation == '4+':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))
    if operation == '4-':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))
    if operation == '4*':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))
    if operation == '4/':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))
        
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '3+':
        print('{} + {} + {} = '.format(number_1, number_2, number_3))
        print(number_1 + number_2 + number_3)

    elif operation == '3-':
        print('{} - {} - {} = '.format(number_1, number_2, number_3))
        print(number_1 - number_2 - number_3)

    elif operation == '3*':
        print('{} * {} * {} = '.format(number_1, number_2, number_3))
        print(number_1 * number_2 * number_3)

    elif operation == '3/':
        print('{} / {} / {} = '.format(number_1, number_2, number_3))
        print(number_1 / number_2 / number_3)

    elif operation == '4+':
        print('{} + {} + {} + {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 + number_2 + number_3 + number_4)

    elif operation == '4-':
        print('{} - {} - {} - {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 - number_2 - number_3 - number_4)

    elif operation == '4*':
        print('{} * {} * {} * {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 * number_2 * number_3 * number_4)

    elif operation == '4/':
        print('{} / {} / {} / {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 / number_2 / number_3 / number_4)

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
        print('Obrigado por baixar e usar meu primeiro software que funciona!')
        quit()
    elif calc_denovo.upper() == 'sim':
        calculate()
    elif calc_denovo.upper() == 'não':
        print('Obrigado por baixar e usar meu primeiro software que funciona!')
        quit()
    elif calc_denovo.upper() == 'nao':
        print('Obrigado por baixar e usar meu primeiro software que funciona!')
        quit()
    elif calc_denovo.upper() == 'Sim':
        calculate()
    elif calc_denovo.upper() == 'Nao':
        print('Obrigado por baixar e usar meu primeiro software que funciona!')
        quit()
    elif calc_denovo.upper() == 'Não':
        print('Obrigado por baixar e usar meu primeiro software que funciona!')
        quit()
    else:
        denovo()

calculate()
#ainda trabalhando em mais atualizações
