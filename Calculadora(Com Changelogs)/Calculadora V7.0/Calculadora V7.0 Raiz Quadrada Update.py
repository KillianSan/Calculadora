import time
import random
from datetime import datetime
now= datetime.now()
def calculate():
    print('Carregando...')
    print(random.randrange(0,20))
    time.sleep(0.25)
    print(random.randrange(20,40))
    time.sleep(0.25)
    print(random.randrange(40,60))
    time.sleep(0.25)
    print(random.randrange(60,80))
    time.sleep(0.25)
    print(random.randrange(80,100))
    time.sleep(0.25)
    print('100% Pronto !!!')
    operation = input('''

   |-------------------------------------------------|              
   | Calculadora do Killian San aka Matilha San V7.0 |
   | Raiz Quadrada Update                            |
   |-------------------------------------------------------------------------------------|
   | Por favor, escolha uma das operações e digite o simbolo dela e depois aperte ENTER: |    
   |----------------------------------------------------------------------------------------------------------------------|                                                                                          
   | (1) CM para Polegadas    | (2) Polegadas para CM       | (3) Verificar se é raiz quadrada|                           |
   | (+) adição               | (-) subtração               | (*) multiplicação               | (/) divisão               |
   | (3+) adição de 3 números | (3-) subtração de 3 números | (3*) multiplicação de 3 números | (3/) divisão de 3 números |
   | (4+) adição de 4 números | (4-) subtração de 4 números | (4*) multiplicação de 4 números | (4/) divisão de 4 números |
   | (horas)                  | (ajuda)                     |                                 |                           |
   |----------------------------------------------------------------------------------------------------------------------|
   | Para reiniciar o programa, digite denovo().                                                                          |
   |----------------------------------------------------------------------------------------------------------------------|

    ''')

    
    if operation == '1':
        number_1 = int(input('Quantos CM ? '))
        time.sleep(0.25)
    elif operation == '+':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
    elif operation == '-':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
    elif operation == '*':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
    elif operation == '/':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
    elif operation == 'sobre':
        print('''Criado por Killian San (A.K.A Matilha San) build 26101911 Calculadora Python v7.0. Tempos de carregamento somente para estética, o programa não precisa desse tempo para carregar porque carrega quase instantâneamente.''')
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == 'horas':
        print(now.hour, now.minute)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == 'que calculadora merda':
        print('... Sério ? ...')
        calculate()
    elif operation == '2':
        number_1 = int(input('Quantas Polegadas ? '))
        time.sleep(0.25)
    elif operation == '3':
        number_1 = int(input('Número para verificar se é raiz: '))
        time.sleep(0.25)
    elif operation == '3+':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
    elif operation == '3-':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
    elif operation == '3*':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
    elif operation == '3/':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
    elif operation == '4+':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.25)
    elif operation == '4-':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.25)
    elif operation == '4*':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.25)
    elif operation == '4/':
        number_1 = int(input('Primeiro Número: '))
        time.sleep(0.25)
        number_2 = int(input('Segundo Número: '))
        time.sleep(0.25)
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.25)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.25)
    elif operation == 'ajuda':
        time.sleep(0.25)
        operation = input('''

  |-----------------------|
  | Bem Vindo a ajuda!!!  |
  |-----------------------------------------------------------------------------------------------------------------------|
  | Escolha uma das operações que você precisa de ajuda, digite símbolo dele e depois aperte ENTER                        |                                                        |
  |-----------------------------------------------------------------------------------------------------------------------|                                                                                          
  | (1) CM para Polegadas    | (2) Polegadas para CM       | (3) verificar se é raiz quadrada| (4) sair da ajuda          |
  | (+) adição               | (-) subtração               | (*) multiplicação               | (/) divisão                |
  | (3+) adição de 3 números | (3-) subtração de 3 números | (3*) multiplicação de 3 números | (3/) divisão de 3 números  |
  | (4+) adição de 4 números | (4-) subtração de 4 números | (4*) multiplicação de 4 números | (4/) divisão de 4 números  |
  |-----------------------------------------------------------------------------------------------------------------------|

            ''')

        if operation == '4':
                calculate()
        elif operation == '+':
            print('''ajuda em adição:

           Na adição o programa irá pedir dois números,
           o "Primeiro Número" e o "Segundo Número", digite dois números e eles serão adicionados, exemplo:

           

           Primeiro Número: 2

           Segundo Número: 2

           2 + 2 = 

           4''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '-':
            print(''' ajuda em subtração:

            Na subtração o programa irá pedir dois números,
            o "Primeiro Número" e o "Segundo Número", digite os dois números e eles serão subtraidos, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            2 - 2 =

            0''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '*':
            print(''' ajuda em multiplicação:

            Na multiplicação o programa irá pedir dois números,
            o "Primeiro Número" e o "Segundo Número", digite os dois números e eles serão multiplicados, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            2 * 2 =

            4''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '/':
            print(''' ajuda em divisão:

            Na divisão o programa irá pedir dois números,
            o "Primeiro Número" e o "Segundo Número", digite os dois números e eles serão divididos, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            2 / 2 =

            1''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '3+':
            print(''' ajuda em adição de 3 números:

            Na adição de 3 números o programa irá pedir 3 números,
            o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão adicionados, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            2 + 2 + 2 =

            6''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '3-':
            print(''' ajuda em subtração de 3 números:

            Na subtração de 3 números o programa irá pedir 3 números,
            o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão subtraidos, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            2 - 2 - 2 =

            -2''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '3*':
            print(''' ajuda em multiplicação de 3 números:

            Na multiplicação de 3 números o programa irá pedir 3 números,
            o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão multiplicados, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            2 * 2 * 2 =

            8''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '3/':
            print(''' ajuda em divisão de 3 números:

            Na divisão de 3 números o programa irá pedir 3 números,
            o "Primeiro Número" o "Segundo Número" e o "Terceiro Número", digite os 3 números e eles serão divididos, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            2 / 2 / 2 =

            0.5''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '4+':
            print(''' ajuda em adição de 4 números:

            Na adição de 4 números o programa irá pedir 4 números,
            o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão adicionados, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            Quarto Número: 2

            2 + 2 + 2 + 2 =

            8''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '4-':
            print(''' ajuda em subtração de 4 números:

            Na subtração de 4 números o programa irá pedir 4 números,
            o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão subtraidos, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            Quarto Número: 2

            2 - 2 - 2 - 2 =

            -4''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '4*':
            print(''' ajuda em multiplicação de 4 números:

            Na multiplicação de 4 números o programa irá pedir 4 números,
            o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão multiplicados, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            Quarto Número: 2

            2 * 2 * 2 * 2 =

            16''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '4/':
            print(''' ajuda em divisão de 4 números:

            Na divisão de 4 números o programa irá pedir 4 números,
            o "Primeiro Número" o "Segundo Número" o "Terceiro Número" e o "Quarto Número", digite os 4 números e eles serão divididos, exemplo:



            Primeiro Número: 2

            Segundo Número: 2

            Terceiro Número: 2

            Quarto Número: 2

            2 / 2 / 2 / 2 =

            0.25'''),
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '1':
            print(''' ajuda com conversão de cm para polegada:

            Na conversão de cm para polegadas o programa irá pedir 2 números e "Quantos cm?",
            digite quantos centímetro a serem convertidos para polegadas no "Quantos cm?", exemplo:


            Quantos cm ? 20

            20 / 2.54 =

            7.874015748031496''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '2':
            print(''' ajuda com conversão de polegadas para cm:

            Na conversão de polegadas para cm o programa irá pedir 2 números e "Quantas Polegadas ?",
            digite quantas polegadas a serem convertidas para cm no "Quantas Polegadas ?", exemplo:


            Quantas Polegadas ? 20

            20 * 2.54 =

            50.8''')
            input('Pressione ENTER para contiunar ...')
            calculate()
        elif operation == '3':
            print(''' ajuda com verificação se o número é raiz de outro

            Na verificação o número digitado pelo usuário é multiplicado por ele mesmo, o número digitado é a raiz do resultado.
            digite o numero que você deseja verificar se é raiz quando a calculadora pedir o "Número para verificar se é raiz: ", exemplo:


            Número para verificar se é raiz: 4

            4 é RAIZ de =
            
            16
            ''')
            input('Pressione ENTER para contiunar ...')
            calculate()

    if operation == '1':
        print('{} / 2.54'.format(number_1, 2.54))
        print(number_1 / 2.54)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '2':
        print('{} * 2.54'.format(number_1, 2.54))
        print(number_1 * 2.54)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '3':
        print('{} é RAIZ de = '.format(number_1, number_1))
        print(number_1 * number_1)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '3+':
        print('{} + {} + {} = '.format(number_1, number_2, number_3))
        print(number_1 + number_2 + number_3)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '4+':
        print('{} + {} + {} + {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 + number_2 + number_3 + number_4)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '3-':
        print('{} - {} - {} = '.format(number_1, number_2, number_3))
        print(number_1 - number_2 - number_3)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '4-':
        print('{} - {} - {} - {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 - number_2 - number_3 - number_4)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '3*':
        print('{} * {} * {} = '.format(number_1, number_2, number_3))
        print(number_1 * number_2 * number_3)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '4*':
        print('{} * {} * {} * {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 * number_2 * number_3 * number_4)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '3/':
        print('{} / {} / {} = '.format(number_1, number_2, number_3))
        print(number_1 / number_2 / number_3)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == '4/':
        print('{} / {} / {} / {} = '.format(number_1, number_2, number_3, number_4))
        print(number_1 / number_2 / number_3 / number_4)
        input('Pressione ENTER para contiunar ...')
        calculate()
    else:
        print('')
        print('Você digitou uma operação inválida, reiniciando...')
        time.sleep(1)
        calculate()
        
def denovo():

    calc_denovo = input('''
  ----------------------------
  || Quer calcular denovo ? ||
  || SIM ou NÃO ?           ||
  ----------------------------
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
