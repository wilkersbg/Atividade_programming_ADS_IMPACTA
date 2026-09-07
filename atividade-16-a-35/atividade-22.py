mediaum = float(input("Digite a nota do aluno: "))
mediadois = float(input("Digite a outra nota do aluno: "))
media = (mediaum + mediadois) / 2
if (mediaum + mediadois) / 2 >= 7:
    print(f"Aprovado {media:.2f}")
elif (mediaum + mediadois) / 2 >= 5:
    print(f"Em Recuperação {media:.2f}")
else:
    print(f"Reprovado {media:.2f}")
