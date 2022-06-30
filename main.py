nome = input("Digite o seu nome: ")

def converterBinario(decimal):
    binario = ''
    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2
    return binario[::-1]


def inverterString(str):
    i = len(str)
    stringInvertida = ''
    while i > 0:
        stringInvertida += str[i - 1]
        i = i - 1  # decrement do índice
        return str  # retorna a string invertida


def converterOctal(decimal):
    octal = ''
    while decimal > 0:
        octal += str(decimal % 8)
        decimal //= 8
    return octal[::-1]


def inverterStrin(str):
    i = len(str)
    stringInvertida = ''
    while i > 0:
        stringInvertida += str[i - 1]
        i = i - 1  # decrement do índice
        return str  # retorna a string invertida


print("Olá olá " + nome + " seja bem vindo a nossa calculadora! ")
print("Por favor escolha a operação que deseja realizar ")
print(''',
      
    OPERAÇÕES DISPONIVEIS:
[1] Decimal para BINÁRIO
[2] Decimal para OCTAL
[3] Decimal para HEXADECIMAL
[4] BINÁRIO para Decimal
[5] OCTAL para Decimal
[6] HEXADECIMAL para Decimal
[7] Potencia = p
[8] Raiz Quadrada da Soma dos Digitos
[+] Para Soma
[-] Para Subtração
[*] Para multiplicação
[/] Para Divisão     
''')
oper = input('Insira a operação: ')

if oper == '1':
    num = int(input("Digite um número em decimal: "))
    print(num, " em binário =: " + inverterString(converterBinario(num)))
# acima a função inverterString() recebe como parâmetro o número binário
# como uma string e faz a conversão
if oper == '2':
    num = int(input("Digite um número em decimal: "))
    print(num, " em Octal  =: " + inverterStrin(converterOctal(num)))
elif oper == '3':
    num=int(input('Digite um número Decimal para conversão.  '))
    hexadecimal=''
    convert ={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

    while(num!=0):
        calculo=num%16
        hexadecimal=convert[calculo]+ hexadecimal
        num=int(num/16)
#RETORNO DO RESULTADO DA CONVERSÃO EM HEXADECIMAL PRO USUARIO
        print('Valor convertido em HEXADECIMAL é',hexadecimal)
if oper == '4':
    num = input('Digite um numero Binário: ')
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) * 2 ** n
        n = n - 1
    print(f'O Binário {num} é igual a {decimal} em decimal')
if oper == '5':
    num = input('Digite um numero Octal: ')
    n = len(num) - 1
    decimal = 0
    for d in num:
        decimal = decimal + int(d) * 8 ** n
        n = n - 1
    print(f'O Octal {num} é igual a {decimal} em decimal')
if oper == '6':
    num = input('Digite um numero Hexadecimal: ')
    n = len(num) - 1
    decimal = 0
    for d in num:
        if d == 'a':
            d = 10
        if d == 'b':
            d = 11
        if d == 'c':
            d = 12
        if d == 'd':
            d = 13
        if d == 'e':
            d = 14
        if d == 'f':
            d = 15
        decimal = decimal + int(d) * 16 ** n
        n = n - 1
    print(f'O Hexadecimal {num} é igual a {decimal} em decimal')
if oper != '1':
    if oper != '2':
        if oper != '3':
            if oper != '4':
              if oper != '5':
                if oper != '6':
                    n1 = float(input('digite um valor: '))
                    n2 = float(input('digite outro valor: '))
if oper == '+':
    print('{} + {} = {}'.format(n1, n2, n1 + n2))
elif oper == '-':
    print('{} - {} = {}'.format(n1, n2, n1 - n2))
elif oper == '*':
    print('{} x {} = {}'.format(n1, n2, n1 * n2))
elif oper == '/':
    print('{} / {} = {}'.format(n1, n2, n1 / n2))
elif oper == '7':
    print('Potencia de {} como base e {} como expoente = {}'.format(n1, n2, n1 ** n2))
elif oper == '8':
    print('A soma de {}+{} é {} e a raiz quadrada de √{} é {}'.format(n1, n2, n1 + n2, n1 + n2, (n1 + n2) ** (1 / 2)))
