# in : savoir si un element existe  dans la liste 
# len : connaître le nombre de caracter dans une chaîne ou  le nombre d'element d'une list
# round() : arondir un decimal a l'entier qui suit
# max() & min() : affiche le plus grand et le plus petit
# sum() : recuperer la somme des element d'une liste valide que pour des entiers
# range() : créer une liste de nombre avec juste un argument allant de zero à l'argument(exclue)
 
etudiants = ["Jack", "Youla", "Kady", "JuuNior", "Fatou"]
element = input("> Entrez votre nom >>")
if element in etudiants:
    print(True) 
    print(etudiants)
else: 
    print(False)
if 'Youla' in etudiants:
    print(">>> Desole vous etez renvoyé ")
    etudiants.remove('Youla')
    print(etudiants)

