# Dans ce projet, vous allez devoir crer un programme qui permette de grer une liste de courses.

# Comme pour la calculatrice, ce projet reviendra plusieurs fois dans la formation avec chaque fois 
# un niveau de difficult supplmentaire.

# Dans cette premire version, on va raliser une version simple de la liste de courses avec la cration 
# d'une liste en mmoire laquelle on ajoute et on enlve des lments.

# La liste ne sera donc pour l'instant pas sauvegarde sur le disque (c'est l'objet de la 2e partie de
# ce projet que vous retrouverez plus tard), mais cela vous permettra de mettre en pratique la gestion 
# des listes et l'interaction avec l'utilisateur ainsi que l'utilisation des boucles.




# creer une liste contenant des elements 
courses = ["Fraise", "Orange", "Candy", "Chocolat", "Miel"]
element = input("Veillez Saisire Le Nom Du Condiment à Ajouter >>:\t")

while element not in courses:
    if len(element) >= 4:
        courses.append(element)
        print("element ajouter a la liste de courses avec succes !!!\n")
        print(courses)
    else: 
        print(input("Nom Trop Court Veillez Saisir A nouveau >>:\t"))
        print("element ajouter a la liste de courses avec succes !!!\n")
        print(courses)  
else:
    print(input("L'element existe déjà dans la liste, Veillez Saisir A nouveau>>:\t"))
    print(element in courses)    
    