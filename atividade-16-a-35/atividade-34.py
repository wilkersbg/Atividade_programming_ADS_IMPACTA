while True:
    mes = int(input("Digite o número do mês (1-12): "))
    ano = int(input("Digite o ano: "))
    bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(f"O mês {mes} tem 31 dias.")
            break
        case 4 | 6 | 9 | 11:
            print(f"O mês {mes} tem 30 dias.")
            break
        case 2:
            if bissexto:
                print(f"O mês {mes} tem 29 dias.")
                break
            else:
                print(f"O mês {mes} tem 28 dias.")
                break
        case _:
            print("Mês inválido. Digite um número entre 1 e 12.")