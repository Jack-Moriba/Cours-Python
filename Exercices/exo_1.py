Salut = "BIENVENUE {name} votre temps moyen d'ecrant est {temps} heures par semaine "
# CALCULATRICE 
a = int(input("Saisir la valeur de premier nombre >> ".title()))
b = int(input("Saisir la valeur de le deuxieme nombre >> ".title()))
if a > 0 or b > 0:
    sum = a , b
    produit =  a * b
    print(sum, produit)
else:
    print("Erreur l'un des nombres saisis est inferieur à 0...\n")