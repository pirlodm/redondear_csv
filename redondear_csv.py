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

# Leer CSV
df = pd.read_csv(archivo, decimal=',')  # separador por defecto ','

# Redondear columnas numéricas
columnas_numericas = df.select_dtypes(include='number').columns
df[columnas_numericas] = df[columnas_numericas].round(2)

# Columnas deseadas en el orden correcto
columnas_deseadas = ['PartidaNumero', 'Fecha Entrada', 'Kilos Pequeños']
columnas_existentes = [c for c in columnas_deseadas if c in df.columns]

# Seleccionar solo las columnas existentes
df = df[columnas_existentes]

# Guardar a Excel
nombre_salida = os.path.splitext(archivo)[0] + '_limpio.xlsx'

with pd.ExcelWriter(nombre_salida, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Datos')
    
    # Formatear como tabla
    workbook  = writer.book
    worksheet = writer.sheets['Datos']
    worksheet.add_table(0, 0, len(df), len(df.columns)-1, {'name': 'TablaDatos', 'columns': [{'header': c} for c in df.columns]})

print(f"✅ Archivo Excel creado correctamente: {nombre_salida}")
