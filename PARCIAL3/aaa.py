import zipfile
import os

ig_path = 'DoubleElectron_Run2012C_0.ig'
extract_dir = 'evento_data'

if not os.path.exists(extract_dir):
    os.makedirs(extract_dir)

try:
    with zipfile.ZipFile(ig_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Archivo descomprimido en: {extract_dir}")
except FileNotFoundError:
    print(f"Archivo no encontrado: {ig_path}")
except zipfile.BadZipFile:
    print(f"El archivo '{ig_path}' no es un archivo ZIP válido.")
