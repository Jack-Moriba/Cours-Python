from pathlib import Path
import shutil
w = Path.home() / "Pathlib" 
w.mkdir(exist_ok=True)
w = w.joinpath("readme.txt")
w.touch(exist_ok=True)
w.write_text("Hello World")
#shutil.rmtree(w)
