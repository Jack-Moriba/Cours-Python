# continue : permet de faire passer la boucle directement à la prochaine itération
# break : permet d'arrêter l'execution complete de la boucle

# IL est aussi possible d'utiliser "else"  avec une boucle for

etudiant = ["Jack", "Youla", "Kady", "JuuNior", "Fatou"]
for prenom in etudiant:
    if prenom == "JuuNior":
        print("JuuNior est trouvé...")
        break
else:
    print('JuuNior est  introuvable')


# any([]) : verifie si au moins une  des condition est respectée et donc vraie
# all([]) : verifie si toutes les conditions sont respectées et donc vraie sinon il nous renvois (False) si une condition est fausse
