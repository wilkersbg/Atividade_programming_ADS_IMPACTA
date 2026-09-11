def contas (a, b):
    mais = a + b
    menos = a - b
    vezes = a * b
    divisao = a / b
    return mais, menos, vezes, divisao

conta = contas(10, 5)
print(f'''
Resultado das contas\n
Soma: {contas(10, 5)[0]}
Subtração: {contas(10, 5)[1]}
Multiplicação: {contas(10, 5)[2]}
Divisão: {contas(10, 5)[3]}
''')
