def calculate():
    operation = input('''
--------------------------------------------------------------------------------------------------
    Calculadora do Killian San aka Matilha San V3.2 (em andamento)

    Update de cores!!! (sem cores por enquanto :/)

    Versão ainda em andamento, se ocorrer bugs, por favor, deixe um comentário no GitHub.
    
    Por favor, escolha uma das operações e digite o simbolo dela e depois aperte ENTER:
    
    (+) adição            | (3+) adição de 3 números        | (4+) adição de 4 números
    
    (-) subtração         | (3-) subtração de 3 números     | (4-) subtração de 4 números
    
    (*) multiplicação     | (3*) multiplicação de 3 números | (4*) multiplicação de 4 números
    
    (/) divisão           | (3/) divisão de 3 números       | (4/) divisão de 4 números


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
        calculate()

    elif operation == '3+':
        print('{} + {} + {} = '.format(number_1, number_2, number_3))
        print(number_1 + number_2 + number_3)
        calculate()

    elif operation == '3-':
        print('{} - {} - {} = '.format(number_1, number_2, number_3))
        print(number_1 - number_2 - number_3)
        calculate()

    elif operation == '3*':
        print('{} * {} * {} = '.format(number_1, number_2, number_3))
        print(number_1 * number_2 * number_3)
        calculate()

    elif operation == '3/':
        print('{} / {} / {} = '.format(number_1, number_2, number_3))
        print(number_1 / number_2 / number_3)
        calculate()

    elif operation == '4+':
        print('{} + {} + {} + {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 + number_2 + number_3 + number_4)
        calculate()

    elif operation == '4-':
        print('{} - {} - {} - {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 - number_2 - number_3 - number_4)
        calculate()

    elif operation == '4*':
        print('{} * {} * {} * {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 * number_2 * number_3 * number_4)
        calculate()

    elif operation == '4/':
        print('{} / {} / {} / {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 / number_2 / number_3 / number_4)
        calculate()

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        calculate()

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        calculate()

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        calculate()

    elif operation == 'adição':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        calculate()

    elif operation == 'subtração':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        calculate()

    elif operation == 'multiplicação':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        calculate()

    elif operation == 'divisão':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        calculate()

    else:
        print('')
        print('Você digitou uma operação inválida, reiniciando...')
        calculate()
        
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
#Versão ainda em andamento, se ocorrer bugs, por favor, deixe um comentário no GitHub
