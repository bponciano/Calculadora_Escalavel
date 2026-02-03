#Calculadora 

#Definindo as operações:
def soma (number1,number2):
    return number1 + number2

def subtracao (number1,number2):
    return number1 - number2

def multiplicacao (number1,number2):
    return number1 * number2

def divisao (number1,number2):
    try:
        valor = number1 / number2
        return valor
            
    except ZeroDivisionError:
        print('Entrada invalida.\nDigite um número diferente de zero.')


operacoes = {'1':soma,'2':subtracao,'3':multiplicacao,'4':divisao}

#Fazendo a leitura dos números e tratando o erro caso o usuario digite uma letra
def ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print('Entrada invalida.\nDigite um número.')

#Cérebro da Calculadora
while True:
    print('----------Calculadora----------\n'
          '1 - Soma\n'
          '2 - Subtração\n'
          '3 - Multiplicação\n'
          '4 - Divisão\n'
          '5 - Sair')
    escolha = input('Escolha umas das opções acima: ')
    
    if escolha == '5':
        print('Programa Encerrado')
        break
    
    if escolha not in operacoes:
        print("Opção invalida.\nPor favor selecionar uma das opções do menu.")
        continue
    number1 = ler_numero('Digite o primeiro valor: ')
    number2 = ler_numero("Digite o segundo valor: ")
    
    acao = operacoes.get(escolha)
    resultado = acao(number1,number2)
    if resultado is not None:
        print(f'O resultado da operação é: {resultado}')