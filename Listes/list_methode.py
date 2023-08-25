# .index() savoir l'index ou le rang ou encore la position d'un element
# .count() savour le nombre d'occurence d'un element 
# .sort() & sorted() trier les elements d'une liste en ordre alphabetique 
# .reverse() afficher une liste du par ordre decroissant du dernier au premier (inverser)
# .pop() supprimer un element et afficher l'element supprimé
# " ".join() joindre les elements de la liste avec un caractere
# .split() separer les element d'une chaîne de caractere sur des espace par defaut (,)
# 

enfants = ["Moïse", "Ami", "Rachelle", "Regina", "Moïse", "Mari"]
#resultat = enfants.index("Rachelle")
#resultat = enfants.count("Moïse")
#resultat = sorted(enfants)
enfants.sort()
#enfants.reverse()
element = enfants.pop(0)

liste = ['Python', 'is', 'an', 'amazing', 'language']
#resultat = " ".join(liste)

fruits = "Avocat, Orange, Fraise, Mangue, Banane"
fruits = fruits.split()



#print(element)
print(enfants)
#print(resultat) 
#print(fruits)
