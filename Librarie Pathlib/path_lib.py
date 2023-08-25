from pathlib import Path    
import shutil

w = Path(r"\Users\theaj\Desktop\Cours Python\json exo\exo_1.json")
print(w.name)
print(w.parent)
print(w.stem)
print(w.suffix)
print(w.suffixes)
print(w.parts)
print(w.exists())
print(w.is_dir())
print(w.is_file())

# Créer et supprimer des dossier avec le module Pathlib
w = Path(r"\Users\theaj\Desktop")
w = w.joinpath("PythonTest")
w.mkdir(exist_ok=True)
w = w / "he" / "she" / 'me'
w.mkdir(parents=True, exist_ok=True)
w = w.joinpath('main.txt')
w.touch()
w.unlink() # supprimer un fichier 
w = w.parent
w.rmdir()
w = w.parent.parent.parent
shutil.rmtree(w) # supprimer un dossier même s'il n'est pas vide  