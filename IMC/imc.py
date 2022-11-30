'''
cette fonction permet de calculer l'indice corporel de masse d'une personne
'''

print("Ce programme vous permet de calculer votre indice corporel de masse")
def calcul_imc():
    poids = float(input("Entrez votre poids kg svp: "))
    taille = float(input("Entrez votre taille en cm svp: "))

    taille2 = taille/100

    imc = round(poids/taille2**2, 1)

    print(f"Votre IMC est: {imc}")
    if imc < 18.5:
        print("Insuffisance pondérale")
    elif 18.5 <= imc < 25:
        print("Corpulence normale")
    elif 25 <= imc < 30:
        print("Surpoids")
    else:
        print("Non prise en charge")
calcul_imc()


