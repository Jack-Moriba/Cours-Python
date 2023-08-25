# .append() permet d'ajouter un seul element à la fois dans une liste
# .extend() permet d'ajouter plusieur element à la fois dans une  liste
# .remove() permet de supprimer un seul element à la fois dans une liste
# .clear() permet de nettoyer tous les elements de la liste
# les slices permetent de recuperer une partie d'une liste des elements specifiques dans une liste
# ils fonctionne de sorte à recuperer les élements se trouvant dans l'intervalle [0:-1] le dernier element etant exclue
# on egalement avoir [::2] ici il recupere tous les elements mais avec un pas de "2" il peux aussi renverser une liste [::-1]
liste = []
print(liste)
liste.append(4)
liste.append(9)
print(liste)
liste.extend([5, 3, 4, 1, 7, 6, 8])
print(liste)
liste.remove(4)
print(liste)
print(liste[2:-1])
print(liste[::2])
print(liste[::-1])
liste.clear()
print(liste)