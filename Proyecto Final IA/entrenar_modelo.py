import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Cargar datos simulados/históricos
df = pd.read_csv("C:/Users/Jerson/Desktop/Proyecto Final IA/datos_entrenamiento.csv")

# Entrenamiento
X = df[["temp", "hum", "mq135"]]
y = df["pm25"]

modelo = LinearRegression()
modelo.fit(X, y)

# Guardar modelo
joblib.dump(modelo, "C:/Users/Jerson/Desktop/Proyecto Final IA/modelo_pm25.pkl")

print("✅ Modelo entrenado y guardado correctamente.")
