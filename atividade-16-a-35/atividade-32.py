while True:
    a = int(input('''digite 1 para segunda-feira
digite 2 para terça-feira
digite 3 para quarta-feira
digite 4 para quinta-feira
digite 5 para sexta-feira
digite 6 para sabado
digite 7 para domingo
digite 8 para sair.
'''))
    match a:
        case 1:
            print('SEGUNDA-FEIRA')
            break
        case 2:
            print('TERÇA-FEIRA')
            break
        case 3:
            print('QUARTA-FEIRA')
            break
        case 4:
            print('QUINTA-FEIRA')
            break
        case 5:
            print('SEXTA-FEIRA')
            break
        case 6:
            print('SABADO')
            break
        case 7:
            print('DOMINGO')
            break
        case 8:
            print('saindo...')
            break
        case _:
            print('número errado, tente novamente')