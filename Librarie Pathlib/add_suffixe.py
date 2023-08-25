from pathlib import Path
from pprint import pprint
w = Path.home() / "Downloads" / "puceau.jpg"
print(w.parent / w.stem)
w = w.parent / (w.stem + "-fière" + w.suffix)
pprint(w)
