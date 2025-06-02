import serial
import pandas as pd
import joblib
import time
import os

# Abrir puerto serial (ajusta si no es COM3)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Esperar que inicie conexión

# Cargar modelo entrenado
modelo = joblib.load("C:/Users/Jerson/Desktop/Proyecto Final IA/modelo_pm25.pkl")

# Ruta CSV para Power BI
csv_path = "C:/Users/Jerson/Desktop/Proyecto Final IA/realtime_data.csv"

# Crear archivo CSV si no existe
if not os.path.exists(csv_path):
    with open(csv_path, "w") as f:
        f.write("temp,hum,mq135,pm25_pred\n")

def leer_datos_serial():
    try:
        linea = ser.readline().decode().strip()
        if linea:
            temp, hum, mq135 = map(float, linea.split(','))
            return temp, hum, mq135
    except:
        pass
    return None

print("⏳ Leyendo datos del Arduino...")

while True:
    datos = leer_datos_serial()
    if datos:
        temp, hum, mq135 = datos
        df = pd.DataFrame([[temp, hum, mq135]], columns=["temp", "hum", "mq135"])
        pm25_pred = modelo.predict(df)[0]

        # Guardar en CSV
        with open(csv_path, "a") as f:
            f.write(f"{temp},{hum},{mq135},{pm25_pred:.2f}\n")

        print(f"📈 PM2.5 Predicho: {pm25_pred:.2f}")
    time.sleep(10)
