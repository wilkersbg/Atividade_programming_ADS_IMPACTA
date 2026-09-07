salario = float(input("Digite seu salario: "))
tempo = int(input('Digite um prazo em anos: '))
valor = float(input('Digite o valor do imóvel: '))

prestacao = valor / (tempo * 12)
limite = salario * 0.30

if prestacao <= limite:
    print("Resultado: EMPRÉSTIMO CONCEDIDO")
else:
    print("Resultado: EMPRÉSTIMO NEGADO")

print(f'''
salario = {salario}
tempo = {tempo}
valor = {valor}
prestacao = {prestacao:.2f}
limite = {limite:.2f}''')