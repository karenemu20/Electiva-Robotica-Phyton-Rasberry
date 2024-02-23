import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def funcion_transferencia_segundo_orden(w_n, zeta):
    num = [w_n**2]
    den = [1, 2 * zeta * w_n, w_n**2]
    return num, den

def tipo_sistema(zeta):
    if zeta < 1:
        return "Subamortiguado"
    elif zeta == 1:
        return "Críticamente Amortiguado"
    else:
        return "Sobreamortiguado"

def graficar_respuesta(t, y, tipo):
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label="Respuesta del sistema")
    plt.title(f"Respuesta del sistema ({tipo})")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Respuesta")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    # Solicitar al usuario los coeficientes
    w_n = float(input("Ingrese la frecuencia natural (w_n) del sistema: "))
    zeta = float(input("Ingrese el coeficiente de amortiguamiento (zeta) del sistema: "))

    # Calcular la función de transferencia
    num, den = funcion_transferencia_segundo_orden(w_n, zeta)

    # Determinar el tipo de sistema
    tipo = tipo_sistema(zeta)
    print(f"El sistema es: {tipo}")

    # Graficar la respuesta del sistema en el tiempo
    t = np.linspace(0, 20, 1000)
    sys = (num, den)
    t, y = signal.step(sys, T=t)
    graficar_respuesta(t, y, tipo)

if __name__ == "__main__":
    main()