precoUnit = float(input('escreva um preço unitario: '))
quantia = int(input('escreva uma quantia: '))
frete = float(input('escreva um frete: '))

print (f'''preço unitario: R$ {precoUnit}
quantia: {quantia}
frete: R$ {frete:.2f}
subtotal: R$ {quantia * precoUnit:.2f}
TOTAL: R$ {quantia * precoUnit + frete:.2f}''')