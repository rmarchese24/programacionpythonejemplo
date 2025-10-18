import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simular mediciones de temperatura
fechas = []
temperaturas = []

for i in range(10):
    fecha = datetime.now().strftime("%d/%m %H:%M:%S")
    temp = round(random.uniform(15.0, 30.0), 2)  # Temperatura entre 15 y 30 grados
    fechas.append(fecha)
    temperaturas.append(temp)

# 2. Crear un DataFrame con pandas
df = pd.DataFrame({
    "Fecha": fechas,
    "Temperatura (°C)": temperaturas
})

# 3. Mostrar la tabla
print("\n📋 Registro de temperaturas:")
print(df)

# 4. Graficar los datos
plt.plot(df["Fecha"], df["Temperatura (°C)"], marker='o', color='green')
plt.title("Temperaturas Registradas")
plt.xlabel("Fecha y hora")
plt.ylabel("Temperatura (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
