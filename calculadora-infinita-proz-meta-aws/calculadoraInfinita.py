def calculadora():
    while True:
        print("Selecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        escolha = input("Opção: ")
        
        if escolha == '0':
            print("Encerrando a calculadora!")
            break
        elif escolha not in ('1', '2', '3', '4'):
            print("Essa opção não existe.")
            continue
        
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        
        if escolha == '1':
            resultado = num1 + num2
        elif escolha == '2':
            resultado = num1 - num2
        elif escolha == '3':
            resultado = num1 * num2
        elif escolha == '4':
            if num2 != 0:
                resultado = round(num1 / num2, 2) 
            else:
                print("Erro: Divisão por zero.")
                continue

        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
