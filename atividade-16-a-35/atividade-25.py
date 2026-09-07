pagamento = float(input("Digite o valor do pagamento: "))
print('''
digite 1 para pagamento em dinheiro ou pix;
digite 2 para pagamento em débito;
digite 3 para pagamento em crédito à vista;
digite 4 para pagamento em crédito parcelado;
digite 5 para sair.
''')
metodo = int(input("Digite o método de pagamento: "))
match metodo:
    case 1:
        print(f'O valor do pagamento é R${pagamento:.2f}, e o desconto é de 10%, portanto o valor final é R$ {pagamento * 0.9:.2f}')
    case 2:
        print(f'O valor do pagamento é R${pagamento:.2f}, e o desconto é de 5%, portanto o valor final é R$ {pagamento * 0.95:.2f}')
    case 3:
        print(f'O valor do pagamento é R${pagamento:.2f}, e o desconto é de 0%, portanto o valor final é R$ {pagamento:.2f}')
    case 4:
        print(f'O valor do pagamento é R${pagamento:.2f}, com acréscimo de 8%, portanto o valor final é R$ {pagamento * 1.08:.2f}')
    case 5:
        print("Saindo do programa.")
        exit()
    case _:
        print("Método de pagamento inválido.")