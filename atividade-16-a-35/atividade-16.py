numero = int(input("Digite um número: "))
if numero > 0:
    print(f"O número {numero} é positivo")
else:
    if numero < 0:
        print(f"O número {numero} é negativo")
    else:
        print(f"O número {numero} é zero")