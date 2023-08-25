from pathlib import Path
from pprint import pprint
# .iterdir() , glob() & rglob() Recupérer tous les fichiers et dossiers à l'interieur d'un dossier 
Path.home().iterdir()
for v in Path.home().iterdir():
    pprint(v.name)

# Affiche les chemin ce vers les fichiers ou dossiers se trouvant à l'interieur d'un dossier
pprint([v for v in Path.home().iterdir() if v.is_dir()])

# Recrpérer certains types de fichiers 
w = Path.home() /"Downloads"
for v in w.rglob("*.mkv"):
    pprint(v.name)