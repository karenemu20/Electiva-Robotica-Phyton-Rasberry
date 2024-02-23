import matplotlib.pyplot as plt
import numpy as np #para generar un rango de temperaturas de -200°C a 200°C con 1000 puntos.

# Definir el rango de temperaturas
temperaturas = np.linspace(-200, 200, 1000)

# Función para calcular la resistencia de un sensor PT100
def calcular_resistencia(temperatura):
    A = 3.9083e-3
    B = -5.775e-7
    R0 = 100.0  # Resistencia a 0°C
    return R0 * (1 + A * temperatura + B * temperatura**2)
#utilizando la ecuación de la curva de calibración PT100.

# Calcular la resistencia para cada temperatura en el rango
resistencias = calcular_resistencia(temperaturas)

# Grafica de resistencias en función de las temperaturas utilizando Matplotlib.
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, color='b', label='Comportamiento del sensor PT100')
plt.title('Comportamiento del sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohm)')
plt.grid(True)
plt.legend()
plt.show()