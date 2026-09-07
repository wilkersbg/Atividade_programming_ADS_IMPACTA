peso = int(input("Digite um peso: "))
altura = float(input("Digite uma altura: "))
IMC = peso / (altura * altura)
if IMC < 18.5:
    print('e você está abaixo da faixa.')
elif 18.5 <= IMC < 25:
    print('e você está a faixa normal.')
elif 25 <= IMC < 30:
    print('e você está acima da faixa.')
else:
    print('e você está com a faixa elevada.')
