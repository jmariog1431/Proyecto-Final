# Sistema Predictivo de Calidad del Aire con Visualización Ambiental

Este proyecto utiliza sensores físicos (DHT11 y MQ-135) conectados a un Arduino para obtener datos de temperatura, humedad y calidad del aire. Un modelo de Machine Learning entrenado en Python predice en tiempo real los niveles de PM2.5, y los datos se visualizan en Power BI.

---

## Componentes del Proyecto

### 1. Hardware (Arduino)

- Sensor DHT11: mide temperatura y humedad.
- Sensor MQ-135: mide calidad del aire (gas).
- Arduino envía datos por puerto serial cada 10 segundos.

### 2. Python (Machine Learning)

- Entrena un modelo con datos históricos para predecir PM2.5.
- Predice valores de PM2.5 en tiempo real usando datos que llegan del Arduino.
- Guarda los datos y predicciones en un archivo CSV para Power BI.

### 3. Power BI

- Visualiza los datos en tiempo real.
- Muestra gráficos de evolución de PM2.5, mapas de calor y alertas ambientales.

---

## Requisitos

- Arduino con sensores DHT11 y MQ-135 configurados.
- Python 3.x instalado.
- Librerías Python: pandas, scikit-learn, pyserial, joblib, matplotlib.
- Power BI Desktop instalado.
- Archivo `modelo_pm25.pkl` (modelo entrenado).
- Archivo `entrenar_modelo.py` para entrenar el modelo.
- Archivo `prediccion_tiempo_real.py` para obtener predicciones en tiempo real.

---

## Instrucciones de Uso

### 1. Entrenar el modelo (solo la primera vez o cuando tengas nuevos datos)

```bash
python entrenar_modelo.py

Ahora conencta tu arduino al puerto com establecido y ejecuta

python prediccion_tiempo_real.py

Se creara un archivo llamado realtime_data.csv

este es el que utilizaras para crear el modelo de power bi
```
