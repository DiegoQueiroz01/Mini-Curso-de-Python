#ano = input("Digite seu ano de nascimento: ") #está sendo lida como string
#ano = int(ano) #converte de string para inteiro
#calculo da idade
#idade = 2025 - ano #faz o cálculo
#print("Sua idade é: ", idade) #imprime o resultado

def calculadora(): #definindo a função calculadora
    print("Operações disponíveis: +  -  *  /  //  %  **") #mostra os operadores disponíveis

    numero1 = float(input("Digite o primeiro número: ")) #inserir o primeiro número podendo ser int ou float
    operador = input("Digite o operador: ") #inserir o operador
    numero2 = float(input("Digite o segundo número: ")) #inserir o segundo número podendo ser int ou float

    if operador == '+': #se soma, faça:
        resultado = numero1 + numero2
    if operador == '-': #se subtração, faça:
        resultado = numero1 - numero2
    if operador == '*': #se multiplicaão, faça:
        resultado = numero1 * numero2
        
    if operador == '/': #se divisão, faça:
        if numero2 != 0: #primeiro número deve ser diferente de zero, então ele realiza essa verificação
            resultado = numero1 / numero2
        else: #se erro, ele imprime a mensagem de erro
            print("Erro: divisão por zero!")
            return
    if operador == '//': #se divisão inteira, faça:
        resultado = numero1 // numero2
    if operador == '%': #se resto da divisão, faça:
        resultado = numero1 % numero2
    if operador == '**': #se exponenciação, faça:
        resultado = numero1 ** numero2
    else: #caso você digite um operador inválido, vai ser imprimida essa mensagem de erro
        print("Operador inválido!")
        return

    print("Resultado:", resultado) #imprime o resultado da operação 

# Chamada da função
calculadora() #chama a função para executar o código
# Fim do código