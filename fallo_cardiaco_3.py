from datasets import load_dataset
import pandas as pd

# Cargamos el counjunto de datos
conjunto_datos = load_dataset("mstz/heart_failure")

datos = conjunto_datos['train']

#  Convertir la estructura de datos en un DataFrame de Pandas
df = pd.DataFrame(datos)

# Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
print("Tipos de Datos en el DataFrame: ")
print(df.dtypes)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).
cantidad_hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]
cantidad_mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)].shape[0]

print(f"\nEl promedio de hombres fumadores es: {cantidad_hombres_fumadores}")
print(f"El promedio de mujeres fumadoras son: {cantidad_mujeres_fumadoras}")
