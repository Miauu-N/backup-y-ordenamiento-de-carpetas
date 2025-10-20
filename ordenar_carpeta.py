from pathlib import Path
import shutil

def ordenar(path):
    folder = Path(path)

    if not folder.exists():
        raise FileNotFoundError(f"La carpeta {folder} no existe")

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()[1:] or "sin_extension"
            dest_folder = folder / ext
            if not dest_folder.exists():
                dest_folder.mkdir()
            shutil.move(file, dest_folder)

    print("Organización completada")

