# On continue avec les jeux et cette fois-ci un projet un peu plus avanc que le simple jeu du nombre mystre.

# Dans ce projet, on va crer un jeu de rle dans le terminal.

# Tu vas te battre contre un ennemi, pouvoir attaquer, prendre une potion et te faire attaquer en retour.

# Beaucoup de choses grer donc !

# Les notions utilises sont les mmes que toutes celles que l'on a vues jusqu' prsent :

#    Dfinir des variables

#    Raliser des oprations mathmatiques

#    Rcuprer la saisie de l'utilisateur

#    Utiliser les boucles

#    Utiliser les modules (notamment le module random)

#    Faire des vrifications (structures conditionnelles)

#    Afficher des informations avec les f-string

# Beaucoup de notions qui l encore individuellement ne sont pas trs complexes, mais que tu vas devoir agencer 
# pour crer ce jeu de rle.

# Ne va pas trop vite, crit les tapes en franais avant de te lancer directement dans du code Python et n'oublie
# pas de tester rgulirement ton code et afficher le type de tes variables pour progresser lentement mais srement !



import random
# Declaration de variable 
Heroe = 1000
Vilain = 1000
attack = 100

a = random.randint(0, 1)


name = input("insert your name >>: ")
print(f"Wellcome {name} \n you're the heroe of this game, you've > {(Heroe)} HP and your attak is {(attack)} ")

# Attack of the heroe
for i in range(10):
    if a == 0:
        print("\nHeroe attack")
        Vilain -= attack
        print(f"Enemie life left >: {Vilain} Hp")
    else: 
        print("\nEnemie attack")
        Heroe -= attack
        print(f"Your life left > {Heroe} Hp")   
        i += 1      
if Heroe == 0 and Vilain > 0:
    print("You lose !!!!!")    
else: 
    print("Congratulation You wine") 