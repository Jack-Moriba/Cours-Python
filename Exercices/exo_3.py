# On continue avec un programme un peu plus marrant que les projets prcdents.

# Dans ce projet, tu vas devoir recrer le jeu du nombre mystre.

# L'ordinateur va choisir un nombre entre 1 et 100 et ton objectif est de trouver ce nombre

# Bien entendu, tu as droit un nombre limit d'essais pour trouver le nombre.

# Tu vas donc devoir utiliser un module que l'on a vu dans les parties prcdentes,
# les boucles, la fonction input.

# Bref, l encore, beaucoup de notions qui individuellement ne sont pas compliques, 
# mais qu'il va falloir que tu saches agencer ensemble dans une logique particulire.


                # Le jeu mystere
# L'ordinateur va choisir un nombre entre 1 et 100 et afficher le nombre
# condition qui limite les des choix

import random

text = "vous n'avez que 5 essaie pour trouver la bonne reponse... Alors bonne chance\n".upper()
print(text)
i = random.randrange(10)
choix = int(input("Quelle est le nombre choisis par  l'ordinateur >>:\t"))
a = 0
while  a in range(5):
    if choix == i:
        print("TOUTES MES FELICITATIONS VOUS AVEZ TROUVÉ")
        break
    elif choix != i:
        print("Desole c'est raté!!!!\n")
        choix = int(input("Veillez reéssayer >>:\t"))
        a += 1
        print("Vos essais sont finis....")
print(f"Le choix de l'ordinateur >>: {i} et Le votre est >>: {choix}")


        