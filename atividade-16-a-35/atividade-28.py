a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")