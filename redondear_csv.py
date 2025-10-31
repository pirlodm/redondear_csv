import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Ocultar ventana principal de Tkinter
Tk().withdraw()

print("Selecciona el archivo CSV que quieres procesar...")
archivo = askopenfilename(filetypes=[("CSV files", "*.csv")])

if not archivo:
    print("No seleccionaste ningún archivo. Saliendo...")
    exit()

# Leer CSV
df = pd.read_csv(archivo, decimal=',', sep=';')

# Redondear columnas numéricas
columnas_numericas = df.select_dtypes(include='number').columns
df[columnas_numericas] = df[columnas_numericas].round(2)

# Seleccionar solo las 3 columnas deseadas
columnas_finales = ['PartidaNumero', 'Fecha Entrada', 'Kilos Pequeños']
df = df[columnas_finales]

# Guardar archivo limpio
nombre_salida = os.path.splitext(archivo)[0] + '_limpio.csv'
df.to_csv(nombre_salida, index=False, sep=';', decimal=',')

print(f"\n✅ Archivo creado correctamente: {nombre_salida}")
input("\nPresiona Enter para salir...")
