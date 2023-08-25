# On revient avec notre projet sur la liste de courses.

# Cette fois-ci, on va avoir un programme un peu plus intressants puisqu'ici on s'intresse la sauvegarde de la liste sur le disque dur.

# Il va donc falloir utiliser ce que vous venez d'apprendre sur les fichiers (et notamment le format JSON) pour lire et crire la liste.

# On commence ainsi pouvoir retenir les donnes au-del de l'excution de notre script, ce que nous reverrons par la suite plus en dtail avec les bases de donnes SQL.


import json

voix = r"C:\Users\theaj\Desktop\Cours Python\json exo\exo_1.json"

with open(voix, "r") as e:
    courses = json.load(e)

element = input("Veillez Saisire Le Nom Du Condiment à Ajouter >>:\t")
while element in courses:
    print("L'element existe déjà dans la liste:")
    print(element)
    break
else:
    if len(element) <= 4:
         print(input("Nom Trop Court, Veillez Saisir A nouveau >>:\t"))
         if element in courses:
            print("L'element existe déjà dans la liste:")
            print(element) 
    else: 
        courses.append(element)
        print("element ajouter a la liste de courses avec succes !!!\n")
        print(courses)

with open(voix, "w") as e:
    json.dump(courses, e, ensure_ascii=False)

#with open(voix, "r") as e:
    #course = json.load(e)
    #print(course)