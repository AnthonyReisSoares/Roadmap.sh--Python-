peso = float(input("Peso: "))
Kg_ou_Lbs = str(input("(K)g ou (L)bs: "))

if Kg_ou_Lbs == (str("k") or str("K")):
    Kg_ou_Lbs = str("Kg")
    print("Peso em " + Kg_ou_Lbs + " " + str(peso))
elif Kg_ou_Lbs == (str("l") or str("L")):
    Kg_ou_Lbs = str("Lbs")
    print("Peso em " + Kg_ou_Lbs + " " + str(peso))
