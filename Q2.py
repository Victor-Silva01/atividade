def pertence_sequencia_fibonacci(numero):
    a, b = 0, 1

    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b

    return False

while True:

    numero_verificado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if pertence_sequencia_fibonacci(numero_verificado):
        print(f"{numero_verificado} pertence à sequência de Fibonacci.")
        break  
    else:
        print(f"{numero_verificado} não pertence à sequência de Fibonacci. Tente novamente.")
