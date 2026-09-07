valor = float(input("Digite um valor: "))
if 0 <= valor <= 1500:
    print(f'{valor} tem um reajuste de 15% e o novo valor é {valor * 1.15:.2f}')
elif 1500 < valor <= 3000:
    print(f'{valor} tem um reajuste de 10% e o novo valor é {valor * 1.10:.2f}')
else:
    print(f'{valor} tem um reajuste de 5% e o novo valor é {valor * 1.05:.2f}')
 