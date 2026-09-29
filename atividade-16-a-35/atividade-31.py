num = int(input('digite um número: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'{num} É DIVISIVEL POR 3 E 5')
elif num % 3 != 0 and num % 5 ==0:
    print(f'{num} É APENAS DIVISIVEL POR 5')
elif num % 3 == 0 and num % 5 != 0:
    print(f'{num} É APENAS DIVISIVEL POR 3')
else:
    print(f'NÃO É DIVISIVEL POR 3 OU 5')