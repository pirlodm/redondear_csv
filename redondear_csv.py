import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Ocultar ventana principal de Tkinter
Tk().withdraw()

# Seleccionar CSV
print("Selecciona el archivo CSV que quieres procesar...")
archivo = askopenfilename(filetypes=[("CSV files", "*.csv")])
if not archivo:
    print("No seleccionaste ningún archivo. Saliendo...")
    exit()

# Leer CSV
df = pd.read_csv(archivo, decimal=',')  # ahora separador por defecto (',') 

# Redondear columnas numéricas
columnas_numericas = df.select_dtypes(include='number').columns
df[columnas_numericas] = df[columnas_numericas].round(2)

# Columnas deseadas en el orden correcto
columnas_deseadas = ['PartidaNumero', 'Fecha Entrada', 'Kilos Pequeños']

# Seleccionar solo las que existen
columnas_existentes = [c for c in columnas_deseadas if c in df.columns]
df = df[columnas_existentes]

if not columnas_existentes:
    print("⚠️ Ninguna de las columnas deseadas existe en este CSV.")
    print("Columnas disponibles en el CSV:", list(df.columns))
else:
    print("Columnas seleccionadas:", columnas_existentes)

# Guardar CSV limpio (separador ',')
nombre_salida = os.path.splitext(archivo)[0] + '_limpio.csv'
df.to_csv(nombre_salida, index=False, decimal=',')  # separador por defecto ','
print(f"\n✅ Archivo creado correctamente: {nombre_salida}")

input("\nPresiona Enter para salir...")
