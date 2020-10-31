def calculate():
    operation = input('''
   |------------------------------------------------------------------------|
   | Calculadora do Killian San aka Matilha San v8.0                        |
   | Remake                                                                 |
   |                                                                        |
   | Build 8.0.311020 (Final)                                               |
   |                                                                        |
   |------------------------------------------------------------------------|
   |Por favor, escolha uma das operacções a digite                          |
   |o simbolo dela depois aperte ENTER.                                     |
   |------------------------------------------------------------------------|
   |+ Adições                            | - Subtrações                     |
   |-------------------------------------|----------------------------------|
   |(+) Adição Simples                   |(-) Subtração Simples             |
   |(3+) Adição de três números          |(3-) Subtração de três números    |
   |(4+) Adição de quatro números        |(4-) Subtração de quatro números  |
   |-------------------------------------|----------------------------------|
   |* Multiplicação                      |/ Divisão                         |
   |-------------------------------------|----------------------------------|
   |(*) Multiplicação Simples            |(/) Divisão Simples               |
   |(3*) Multiplicação de três números   |(3/) Divisão de três números      |
   |(4*) Multiplicação de quatro números |(4/) Divisão de quatro números    |
   |-------------------------------------|----------------------------------|
   | Operações Diversas                                                     |
   |------------------------------------------------------------------------|
   |(1) CM para Polegadas                |(2) Polegadas para CM             |
   |(ajuda)                              |(sobre)                           |      
   |-------------------------------------|----------------------------------|
    
   
''')


    if operation == '1':
        n1 = int(input('Quantos CM ? '))
    elif operation == '2':
        n1 = int(input('Quantas Polegadas ? '))
    elif operation == '+':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
    elif operation == '3+':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
    elif operation == '4+':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
        n4 = int(input('Quarto Número: '))
    elif operation == '-':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
    elif operation == '3-':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
    elif operation == '4-':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
        n4 = int(input('Quarto Número: '))
    elif operation == '*':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
    elif operation == '3*':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
    elif operation == '4*':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
        n4 = int(input('Quarto Número: '))
    elif operation == '/':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
    elif operation == '3/':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
    elif operation == '4/':
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segúndo Número: '))
        n3 = int(input('Terceiro Número: '))
        n4 = int(input('Quarto Número: '))
    elif operation == 'sobre':
        print('''Criado por: Killian San Calculadora Python V8.0 Obrigado por baixar!!!''')
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == 'ajuda':
        print('A ajuda se encontra no arquivo ajudaV8.txt na mesma pasta da CalculadoraV8')
        input('Pressione ENTER para continuar...')
        calculate()
    if operation == '1':
        print('{} / 2.54' .format(n1, 2.54))
        print(n1 / 2.54)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '2':
        print('{} * 2.54' .format(n1, 2.54))
        print(n1 * 2.54)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '+':
        print('{} + {} = ' .format(n1, n2))
        print(n1 + n2)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '3+':
        print('{} + {} + {} = ' .format(n1, n2, n3))
        print(n1 + n2 + n3)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '4+':
        print('{} + {} + {} + {} = ' .format(n1, n2, n3, n4))
        print(n1 + n2 + n3 + n4)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '-':
        print('{} - {} = ' .format(n1, n2))
        print(n1 - n2)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '3-':
        print('{} - {} - {} = ' .format(n1, n2, n3))
        print(n1 - n2 - n3)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '4-':
        print('{} - {} - {} - {} = ' .format(n1, n2, n3, n4))
        print(n1 - n2 - n3 - n4)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '*':
        print('{} * {} = ' .format(n1, n2))
        print(n1 * n2)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '3*':
        print('{} * {} * {} = ' .format(n1, n2, n3))
        print(n1 * n2 * n3)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '4*':
        print('{} * {} * {} * {} = ' .format(n1, n2, n3, n4))
        print(n1 * n2 * n3 * n4)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '/':
        print('{} / {} = ' .format(n1, n2))
        print(n1 / n2)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '3/':
        print('{} / {} / {} = ' .format(n1, n2, n3))
        print(n1 / n2 / n3)
        input('Pressione ENTER para continuar...')
        calculate()
    elif operation == '4/':
        print('{} / {} / {} / {} = ' .format(n1, n2, n3, n4))
        print(n1 / n2 / n3 / n4)
        input('Pressione ENTER para continuar...')
        calculate()
    else:
        print('')
        print('Você digitou uma operação inválida, reiniciando...')
        calculate()

def denovo():

    calc_denovo = input('''
   Quer calcular denovo ?
   
        S ou N ?

        ''')

    if calc_denovo.upper() == 's':
        calculate()
    elif calc_denovo.upper() == 'S':
        calculate()
    elif calc_denovo.upper() == 'n':
        print('Obrigado por baixar e usar a Calculadora V8.0, fique ligado para futuros updates!')
        quit
    elif calc_denovo.upper() == 'N':
        print('Obrigado por baixar e usar a Calculadora V8.0, fique ligado para futuros updates!')
        quit
        
calculate() 
