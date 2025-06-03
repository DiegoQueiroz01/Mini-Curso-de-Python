def calculadora (): #definir a função
    print("Calculadora Simples")

    print("Operações disponíveis: + , -, *, /, //, **, %") #definir as operações que vamos ter na cálculadora

    numero1 = float(input("Digite o primeiro número: ")) #inserir o primeiro número que ele deseja
    operador = input("Escolha o operador: ") #operador que ele deseja na função
    numero2 = float(input("Digite o segundo número: ")) #inserir o segundo número

    #Estruturas de condições
    if operador == "+": #se o operadorador for igual a soma, então...
        resultado = numero1 + numero2
    if operador == "-": #se o operador for igual a subtração, então...
        resultado = numero1 - numero2
    if operador == "*":
        resultado = numero1 * numero2
    if operador == "/":
        if numero2 == 0: #verificar se o segundo número é igual a zero.
            print("Erro: Divisão por zero não é permitido.")
        resultado = numero1 / numero2
    if operador == "//":
        resultado = numero1 // numero2
    if operador == "**":
        resultado = numero1 ** numero2
    if operador == "%":
        resultado = numero1 % numero2

    else:
        print("Operador inválido. Tente novamente.") #caso ele corra o código, e não reconheça nenhuma condição, ele vai cair aqui
    return #reinicia o codigo
    
    print("Resultado: ", resultado) #imprime o resultado da operação

#Chamar a função
calculadora() #chamar novamente a função para reiniciar o código
#Fim do código
    