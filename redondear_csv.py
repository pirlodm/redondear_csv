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
df = df[columnas_existentes]

# Crear carpeta 'limpio' en la misma ruta del CSV original
carpeta_salida = os.path.join(os.path.dirname(archivo), 'limpio')
os.makedirs(carpeta_salida, exist_ok=True)

# Guardar Excel con mismo nombre dentro de la carpeta 'limpio'
nombre_salida = os.path.join(carpeta_salida, os.path.splitext(os.path.basename(archivo))[0] + '.xlsx')

with pd.ExcelWriter(nombre_salida, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Datos')
    
    # Formatear como tabla
    workbook  = writer.book
    worksheet = writer.sheets['Datos']
    worksheet.add_table(0, 0, len(df), len(df.columns)-1, 
                        {'name': 'TablaDatos', 'columns': [{'header': c} for c in df.columns]})

print(f"✅ Archivo Excel creado correctamente: {nombre_salida}")
