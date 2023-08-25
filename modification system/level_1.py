import json
# soit on inverse le sens des slish (/) soit on precede par (r"") soit on double les shish (\\)
#chemin = "C:\\Users\\theaj\\Desktop\\Cours Python\\file.json"
#print(chemin)

# "r" (read = lire), "w" (write = ecrire mais ecrasser le contenu existant); 
# "a"( appened = ajouter  sans ecraser le contenu existant)
# ".seek()" permet d'indiquer a  partir de quel niveau il faut lire (changer la position du curseur à la lecture ou l'affichage)
# "ensure_ascii=False" permet d'afficher les excentuations et les caractères speciaux

# with open(chemin, "a") as a:
#   a.write("\nHello")

# with open(chemin, "r") as a:
 #  fond = a.read()
  #  print(fond)

# ecrire à l'interieur d'un fichier json (on utilise la methode json.dump)
chemin = r"C:\Users\theaj\Desktop\Cours Python\modification system\file.json"

with open(chemin, "w") as a:
     json.dump(list(range(10)), a, indent=4)
    #liste = json.load(a)
    #print(type(liste))


# Modiffier un fichier json 
road = r"C:\Users\theaj\Desktop\Cours Python\modification system\modif.json"

with open(road, "w") as j:
    json.dump(list(range(15)), j, indent=4 )

with open(road, "r") as j:
    data = json.load(j)

data.append(15)

with open(road, "w") as j:
    json.dump(data, j, indent=4)



    