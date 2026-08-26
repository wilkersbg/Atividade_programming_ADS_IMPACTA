salarioFixo = float(input('quando  você ganha por mês? '))
totalVendido = float(input('quanto você vendeu esse mês? '))

print(f''' salario fixo: R$ {salarioFixo:.2f}
total vendido: R$ {totalVendido:.2f}
comissão: R$ {totalVendido * 0.04:.2f}
salario atual: R$ {totalVendido * 0.04 + salarioFixo:.2f}''')