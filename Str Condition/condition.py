# LES STRUCTURE CONDIONNELLES (if,elif & else) Les OPPERATEURS LOGIQUES (and, or, not)
note = input("veillez saisir votre note >>".title())
max = 20
if int(note) > 5 and  int(note) < 10:
    print("Vous avez encore du chemin".upper())
elif int(note) >= 10  and  int(note) < 13:
    print("pas mal vous êtes passable".upper())
elif int(note) >= 13  and  int(note) <= 15:
    print("bien jouer vous apprenez vite".upper())
elif int(note) > 15 and int(note) <= max:
    print("excellent vous êtes un pro".upper())
elif int(note) > max:
    print("Erreur de saisis veillez reéssayer".upper())
else:
    print("mediocre vous avez beaucoup a apprendre".upper())
print(f"votre note est> {note}")
