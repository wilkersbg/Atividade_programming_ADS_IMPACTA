idade = int(input("Quantos anos você tem? "))
if idade < 16:
    print("Você não pode votar.")
elif idade in (16, 17) or idade > 70:
    print("O voto é opcional para você.")
else:
    print("O voto é obrigatório para você.")