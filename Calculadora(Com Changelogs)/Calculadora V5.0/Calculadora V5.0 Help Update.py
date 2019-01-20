def calculate():
    operation = input('''
---------------------------------------------------------------------------------------------
    Calculadora do Killian San aka Matilha San V5.0.1

    "Help Update"
---------------------------------------------------------------------------------------------
    Por favor, escolha uma das operações e digite o simbolo dela e depois aperte ENTER:       
                                                                                              
    (+) adição            | (3+) adição de 3 números        | (4+) adição de 4 números        
                                                                                              
    (-) subtração         | (3-) subtração de 3 números     | (4-) subtração de 4 números
    
    (*) multiplicação     | (3*) multiplicação de 3 números | (4*) multiplicação de 4 números
    
    (/) divisão           | (3/) divisão de 3 números       | (4/) divisão de 4 números

    (1) cm para polegadas | (2) polegadas para cm           | (3) Raiz Quadrada

    (4) ajuda             |

    para as operações (1),(2) e ajuda digite 0 no "Primeiro Número" e no "Segundo Número".
---------------------------------------------------------------------------------------------

        Para reiniciar o programa, digite denovo().
    ''')
    
    number_1 = int(input('Primeiro Número: '))
    number_2 = int(input('Segundo Número: '))
    if operation == '3':
        number_1 = int(input('Número para pegar a raiz : '))

    elif operation == '3+':
        number_3 = int(input('Terceiro Número: '))

    elif operation == '3-':
        number_3 = int(input('Terceiro Número: '))

    elif operation == '3*':
        number_3 = int(input('Terceiro Número: '))

    elif operation == '3/':
        number_3 = int(input('Terceiro Número: '))

    elif operation == '4+':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))

    elif operation == '4-':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))

    elif operation == '4*':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))

    elif operation == '4/':
        number_3 = int(input('Terceiro Número :'))
        number_4 = int(input('Quarto Número: '))

    elif operation == '1':
        number_1 = int(input('Quantos Cm ? '))

    elif operation == '2':
        number_1 = int(input('Quantas polegadas ? '))

    elif operation == 'ajuda':
        operation = input('''
        
        Bem Vindo a ajuda!!!

        Escolha uma das operações que você precisa de ajuda, digite símbolo dele e depois aperte ENTER

            (+) adição            | (3+) adição de 3 números        | (4+) adição de 4 números        
                                                                                              
            (-) subtração         | (3-) subtração de 3 números     | (4-) subtração de 4 números
    
            (*) multiplicação     | (3*) multiplicação de 3 números | (4*) multiplicação de 4 números
    
            (/) divisão           | (3/) divisão de 3 números       | (4/) divisão de 4 números

            (1) cm para polegadas | (2) polegadas para cm           | (3) Raiz Quadrada 
            
            (4) sair da ajuda     |
            ''')
        if operation == '4':
                calculate()
        elif operation == '+':
            print('''ajuda em adição:
           Na adição o programa irá pedir dois números, o "Primeiro Número" e o "Segundo Número", digite dois números e eles serão adicionados, exemplo:
           
           Primeiro Número: 2
           Segundo Número: 2
           2 + 2 = 
           4''')
            calculate()
        elif operation == '-':
            print(''' ajuda em subtração:
            Na subtração o programa irá pedir dois números, o "Primeiro Número" e o "Segundo Número", digite os dois números e eles serão subtraidos, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            2 - 2 =
            0''')
            calculate()
        elif operation == '*':
            print(''' ajuda em multiplicação:
            Na multiplicação o programa irá pedir dois números, o "Primeiro Número" e o "Segundo Número", digite os dois números e eles serão multiplicados, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            2 * 2 =
            4''')
            calculate()
        elif operation == '/':
            print(''' ajuda em divisão:
            Na divisão o programa irá pedir dois números, o "Primeiro Número" e o "Segundo Número", digite os dois números e eles serão divididos, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            2 / 2 =
            1''')
            calculate()
        elif operation == '3+':
            print(''' ajuda em adição de 3 números:
            Na adição de 3 números o programa irá pedir 3 números, o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão adicionados, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            2 + 2 + 2 =
            6''')
            calculate()
        elif operation == '3-':
            print(''' ajuda em subtração de 3 números:
            Na subtração de 3 números o programa irá pedir 3 números, o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão subtraidos, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            2 - 2 - 2 =
            -2''')
            calculate()
        elif operation == '3*':
            print(''' ajuda em multiplicação de 3 números:
            Na multiplicação de 3 números o programa irá pedir 3 números, o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão multiplicados, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            2 * 2 * 2 =
            8''')
            calculate()
        elif operation == '3/':
            print(''' ajuda em divisão de 3 números:
            Na divisão de 3 números o programa irá pedir 3 números, o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão divididos, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            2 / 2 / 2 =
            0.5''')
            calculate()
        elif operation == '4+':
            print(''' ajuda em adição de 4 números:
            Na adição de 4 números o programa irá pedir 4 números, o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão adicionados, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            Quarto Número: 2
            2 + 2 + 2 + 2 =
            8''')
            calculate()
        elif operation == '4-':
            print(''' ajuda em subtração de 4 números:
            Na subtração de 4 números o programa irá pedir 4 números, o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão subtraidos, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            Quarto Número: 2
            2 - 2 - 2 - 2 =
            -4''')
            calculate()
        elif operation == '4*':
            print(''' ajuda em multiplicação de 4 números:
            Na multiplicação de 4 números o programa irá pedir 4 números, o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão multiplicados, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            Quarto Número: 2
            2 * 2 * 2 * 2 =
            16''')
            calculate()
        elif operation == '4/':
            print(''' ajuda em divisão de 4 números:
            Na divisão de 4 números o programa irá pedir 4 números, o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão divididos, exemplo:

            Primeiro Número: 2
            Segundo Número: 2
            Terceiro Número: 2
            Quarto Número: 2
            2 / 2 / 2 / 2 =
            0.25'''),
            calculate()
        elif operation == '1':
            print(''' ajuda com conversão de cm para polegada:
            Na conversão de cm para polegadas o programa irá pedir 2 números e "Quantos cm?", digite 0 nos "Primeiro Número" e "Segundo Número" e digite quantos centímetro a serem convertidos para polegadas no "Quantos cm?", exemplo:

            Primeiro Número: 0
            Segundo Número: 0
            Quantos cm ? 20
            20 / 2.54 =
            7.874015748031496''')
            calculate()
        elif operation == '2':
            print(''' ajuda com conversão de polegadas para cm:
            Na conversão de polegadas para cm o programa irá pedir 2 números e "Quantas Polegadas ?", digite 0 nos "Primeiro Número" e "Segundo número" e digite quantas polegadas a serem convertidas para cm no "Quantas Polegadas ?", exemplo:

            Primeiro Número: 0
            Segundo Número: 0
            Quantas Polegadas ? 20
            20 * 2.54 =
            50.8''')
            calculate()
        elif operation == '3':
            print(''' não funciona ainda, fique ligado na próxima atualização''')
            calculate()

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        calculate()

    elif operation == '3':
        print('{} RAIZ = '.format(number_1))
        print(number_1 / 4)
        calculate()

    elif operation == '1':
        print('{} / 2.54'.format(number_1, 2.54))
        print(number_1 / 2.54)
        calculate()

    elif operation == '2':
        print('{} * 2.54'.format(number_1, 2.54))
        print(number_1 * 2.54)
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
    elif calc_denovo.upper() == 'n':
        print('Obrigado por baixar e usar meu primeiro software que funciona!')
        quit()
    elif calc_denovo.upper() == 's':
        calculate()
        
    else:
        denovo()

calculate()
#Versão ainda em andamento, se ocorrer bugs, por favor, deixe um comentário no GitHub
