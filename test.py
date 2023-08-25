print("hello World")

# Les fonctions 
str("") # chaînes de caracteres 
int()   # Les Entiers
float() # Les decimaux
bool()  # Les verification True or False

# Les Variables 
print("I am Jack")
a = 4
b = "20"
b = int(b) # Change le type de la variable
print(a + b)

# la fonction type permet d'afficher le type d'une variable
print(type(a))

# Recuperation de saisis de l'utilisateur
user = input("votre age >>")
print("votre age est:" + user)

# Changer la case d'une chaîne de caractere
# .upper() = Mettre toute la phase en Majuscule
c = "my name is jack".upper()
print(c)
# .lower() = Mettre toutes la phrase en minuscule
v = "my name is jack".lower()
print(v)
# .capitalize() = Mettre la premiere lettres en maj
d = "my name is jack".capitalize()
print(d) 
# .title() = Mettre toutes les premiere lettres en maj
s = 'my name is jack'.title()
print(s) 
# Remplacer un ou plusieurs elements ( .replace & .strip)
# .replace = remplacer un mot par un autre 
e = "my name is jack".replace("name", "nom")
print(e)
# .strip() = Supprimer les Espace mais sert aussi à supprimer les lettres 
e = "  my name is jack  ".strip()
print(e)
e = "  my name is jack  ".rstrip(" jcak ")
print(e)
e = "  my name is jack  ".lstrip(" nema ")
print(e)
# SEPARER ET JOINDRE  (joint & split)
e = "-".join(['1', '3', '4', '5', '6'])
print(e)
e = '1, 2, 3, 4, 5, 6,'.split(', ')
print(e)
# REMPLIRE DE ZEROS  (zfill)
i = '9'.zfill(3)
print(i)
#
for i in range(100):
    print(str(i).zfill(3))
# LES METHODES "is"
'Bonjour'.islower()
'45f'.isdigit() # Veriffie si une chaîne de caractere ne contient que des chiffres
# COMPTER LES OCCURRENCES (count)
'Bonjour le jour'.count('jour')
# TROUVER UNE CHAINE ( find & index)
'Bonjour le jour'.find('jour') # on peut aussi utiliser (rfind & lfind)
'Bonjour le jour'.index('jour')
# VERIFIER LA TERMINAISON OU LE DEBUT
'Bonjour le jour'.startswith('our')
False
'Bonjour le jour'.endswith('our')
True
# INSERER UN CHIFFRE DANS UNE CHAINE DE CARACTERE (format() & f"")
age = 21
print("J'ai {age} ans".format(age = age))
Prenom = "Jack"
age = 21
print("Je m'appel {}  et j'ai {} ans".format(Prenom,age))
n = 23 
m = 6
print(f"On donne les nombre a = {m} et b = {n} dont la somme S = {m + n} et le produit P = {m * n}")


from Exercices.exo_1 import Salut
user = input("Veillez saisir votre nom >>>")
time = age
Acceuille = Salut.format(name=user, temps=time)
print(Acceuille)


