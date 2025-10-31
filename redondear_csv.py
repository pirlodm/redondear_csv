import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Ocultar ventana principal de Tkinter
Tk().withdraw()

# Seleccionar CSV
archivo = askopenfilename(filetypes=[("CSV files", "*.csv")], title="Selecciona el archivo CSV")
if not archivo:
    exit()  # salir si no seleccionó ningún archivo

# Leer CSV (decimal con coma)
df = pd.read_csv(archivo, decimal=',')  # separador por defecto ','

# Redondear columnas numéricas
columnas_numericas = df.select_dtypes(include='number').columns
df[columnas_numericas] = df[columnas_numericas].round(2)

# Columnas deseadas en el orden correcto
columnas_deseadas = ['PartidaNumero', 'Fecha Entrada', 'Kilos Pequeños']
columnas_existentes = [c for c in columnas_deseadas if c in df.columns]

# Seleccionar solo las columnas existentes
df = df[columnas_existentes]

# Guardar CSV limpio en la misma carpeta que el original
nombre_salida = os.path.splitext(archivo)[0] + '_limpio.csv'
df.to_csv(nombre_salida, index=False, decimal=',')  # separador por defecto ','

# Mensaje final
print(f"✅ Archivo creado correctamente: {nombre_salida}")
