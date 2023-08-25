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
        continue
    else: 
        print("\nEnemie attack")
        Heroe -= attack
        print(f"Your life left > {Heroe} Hp")   
        i += 1      
if Heroe == 0 and Vilain > 0:
    print("You lose !!!!!")    
else: 
    print("Congratulation You wine") 