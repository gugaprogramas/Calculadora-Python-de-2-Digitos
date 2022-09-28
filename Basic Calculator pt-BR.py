def calcular():
    operacao = input('''
Escolha uma das operações matemáticas a seguir:
+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão
''')

    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    # adição
    if operacao == '+':
        print('{} + {}'.format(n1, n2))
        print(n1 + n2)
    
    # subtração
    elif operacao == '-':
        print('{} - {}'.format(n1, n2))
        print(n1 - n2)

    # multiplicação
    elif operacao == '*':
        print('{} * {}'.format(n1, n2))
        print(n1 * n2)

    # divisão
    elif operacao == '/':
        print('{} / {}'.format(n1, n2))
        print(n1 / n2)

    else:
        print('Voce não utilizou um dos operadores listados acima!!')
              
    calcular()
  
    
calcular()

