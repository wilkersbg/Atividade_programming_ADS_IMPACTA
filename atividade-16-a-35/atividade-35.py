idade = int(input("Digite sua idade: "))
estuda = input("Você estuda? (sim/não): ")
preco = 30
if idade <= 12 or idade >= 60 or estuda.lower() == "sim":
    print(f"Você tem direito a meia-entrada. {preco / 2} reais.")
else:
    print(f"Você não tem direito a meia-entrada. {preco} reais.")