def inverter_string(numero):
    invertida = ""
    for i in range(len(numero) - 1, -1, -1):
        invertida += numero[i]
    return invertida

while True:
    entrada = input("Digite uma numero para inverter: ")
    resultado = inverter_string(entrada)
    print("String original:", entrada)
    print("String invertida:", resultado)
    continuar = input("Deseja inverter outra numero? (sim/não): ").lower()

    if continuar != 'sim':
        break  
