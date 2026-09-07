a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Resultado: FORMAM UM TRIÂNGULO EQUILÁTERO")
    elif a == b or b == c or a == c:
        print("Resultado: FORMAM UM TRIÂNGULO ISÓSCELES")
    elif a != b and b != c and a != c:
        print("Resultado: FORMAM UM TRIÂNGULO ESCALENO")
else:
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")