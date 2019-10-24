import time
import random
from decimal import *
from datetime import datetime
now= datetime.now()
def calculate():
    print('Carregando...')
    print(random.randrange(0,20))
    time.sleep(1)
    print(random.randrange(20,40))
    time.sleep(1)
    print(random.randrange(40,60))
    time.sleep(1)
    print(random.randrange(60,80))
    time.sleep(1)
    print(random.randrange(80,100))
    time.sleep(1)
    print('100% Pronto !!!')
    operation = input('''

   |-------------------------------------------------|              
   | Calculadora do Killian San aka Matilha San V6.0 |
   | A e s t h e t i c   u p d a t e                 | 
   |-------------------------------------------------------------------------------------|
   | Por favor, escolha uma das operações e digite o simbolo dela e depois aperte ENTER: |    
   |----------------------------------------------------------------------------------------------------------------------|                                                                                          
   | (1) CM para Polegadas    | (2) Polegadas para CM       |  horas                          |  ajuda                    |
   | (+)adição                | (-) subtração               | (*) multiplicação               | (/) divisão               |
   | (3+) adição de 3 números | (3-) subtração de 3 números | (3*) multiplicação de 3 números | (3/) divisão de 3 números |
   | (4+) adição de 4 números | (4-) subtração de 4 números | (4*) multiplicação de 4 números | (4/) divisão de 4 números |
   |----------------------------------------------------------------------------------------------------------------------|
   | para as operações (1),(2) e ajuda digite quantos cm ou polegadas no "Primeiro Número"                                |
   | e no "Segundo Número" digite 0.                                                                                      |
   |----------------------------------------------------------------------------------------------------------------------|
   | Para reiniciar o programa, digite denovo().                                                                          |
   |----------------------------------------------------------------------------------------------------------------------|

    ''')

    

    number_1 = int(input('Primeiro Número: '))
    time.sleep(1)
    number_2 = int(input('Segundo Número:'))
    time.sleep(1)
    if operation == '1':
        time.sleep(1)
    elif operation == 'sobre':
        print('Criado por Killian San (A.K.A Matilha San) build 2410.2019 Calculadora Python v6.0. Tempos de carregamento somente para estética, o programa não precisa desse tempo para carregar porque carrega quase instantâneamente.')
        calculate()
    elif operation == 'horas':
        print(now.hour, now.minute)
        input('Pressione ENTER para contiunar ...')
        calculate()
    elif operation == 'que calculadora merda':
        print('... Sério ? ...')
        calculate()
    elif operation == '2':
        time.sleep(1)
    elif operation == '3':
        number_1 = int(input('Número para pegar a raíz: '))
        time.sleep(1)
    elif operation == '3+':
        number_3 = int(input('Terceiro Número: '))
        time.sleep(1)
    elif operation == '3-':
        number_3 = inr(input('Terceiro Número: '))
        time.sleep(1)
    elif operation == '3*':
        number_3 = int(input('terceiro Número: '))
        time.sleep(1)
    elif operation == '3/':
        number_3 = int(input('Terceiro Número: '))
        time.sleep(1)
    elif operation == '4+':
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.5)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.5)
    elif operation == '4-':
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.5)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.5)
    elif operation == '4*':
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.5)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.5)
    elif operation == '4/':
        number_3 = int(input('Terceiro Número: '))
        time.sleep(0.5)
        number_4 = int(input('Quarto Número: '))
        time.sleep(0.5)
    elif operation == 'ajuda':
        time.sleep(1)
        operation = input('''

  |-----------------------|
  | Bem Vindo a ajuda!!!  |
  |-----------------------------------------------------------------------------------------------------------------------|
  | Escolha uma das operações que você precisa de ajuda, digite símbolo dele e depois aperte ENTER                        |                                                        |
  |------------------------------------------------------------------------------------------------------------------------                                                                                           
  | (1) CM para Polegadas    | (2) Polegadas para CM       | (4) sair da ajuda               |                            |
  | (+)adição                | (-) subtração               | (*) multiplicação               | (/) divisão                |
  | (3+) adição de 3 números | (3-) subtração de 3 números | (3*) multiplicação de 3 números | (3/) divisão de 3 números  |
  | (4+) adição de 4 números | (4-) subtração de 4 números | (4*) multiplicação de 4 números | (4/) divisão de 4 números  |
  |-----------------------------------------------------------------------------------------------------------------------|

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
        print('{} RAIZ = '.format(number_1, 2.54))
        print(number_1 / 2.54)
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
        print('{} - {} - {} - {] = '.format(number_1, number_2, number_3, number_4))
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
