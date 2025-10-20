from pathlib import Path
from datetime import datetime
import shutil
import schedule
import time



def crear_backup(path, backups_path):
    if not backups_path.exists():
        backups_path.mkdir()

    fecha = datetime.now().strftime("%d-%m-%Y-%H-%M")
    backup = backups_path / f"{path.name} - {fecha}"
    print(f"realizando backup {backup}")
    try:
        shutil.copytree(path,backup)
    except Exception as e:
        print(f"error al generar el backup, exception: {e}")



def borrar_b(bp):
    menor = None
    archivo = False
    if bp.exists():
        dirs = list(bp.iterdir())
        if len(dirs) > 0:
            for b in dirs:
                if menor is None or b.stat().st_mtime < menor:
                    menor = b.stat().st_mtime
                    archivo = b
        if archivo:
            print(f"borrando {archivo.name}")
            try:
                shutil.rmtree(archivo)
            except Exception as e:
                print(f"error al borrar el backup: {e}")

def controlar_backups(bp , limite):
    if not bp.exists():
        raise Exception("la carpeta de backups no existe")
    k = 0
    for _ in bp.iterdir():
        k += 1
    if k > limite:
        for _ in range(k-limite):
            borrar_b(bp)


def registrar_backup(path,bp,lim):
    path = Path(path)
    backups_path = Path(bp)
    schedule.every(1).days.do(lambda: crear_backup(path,backups_path))
    schedule.every(1).days.do(lambda: controlar_backups(backups_path,lim))
    while True:
        schedule.run_pending()
        time.sleep(60)
