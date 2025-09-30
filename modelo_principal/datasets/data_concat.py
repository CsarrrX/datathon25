import pandas as pd

# El archivo está en la subcarpeta 'data'
ruta_dataset = "03_IBD_GTstudentproject_test.csv"

try:
    df = pd.read_csv(ruta_dataset)
    print("Archivo leído exitosamente.")
    print(df.head()) # Muestra las primeras 5 filas del DataFrame
except FileNotFoundError:
    print(f"Error: El archivo '{ruta_dataset}' no se encontró.")