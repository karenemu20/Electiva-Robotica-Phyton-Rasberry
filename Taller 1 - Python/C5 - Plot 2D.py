import matplotlib.pyplot as plt

# Función para dibujar el nombre 'KAREN'
def dibujar_nombre_karen():
    plt.text(0.1, 0.5, 'K', fontsize=100, color='blue')
    plt.plot([0.2, 0.2], [0.3, 0.7], color='blue')
    plt.plot([0.2, 0.4], [0.7, 0.3], color='blue')
    plt.plot([0.4, 0.4], [0.3, 0.7], color='blue')

# Función para dibujar el nombre 'DIANA'
def dibujar_nombre_diana():
    plt.text(0.6, 0.5, 'D', fontsize=100, color='green')
    plt.plot([0.7, 0.7], [0.3, 0.7], color='green')
    plt.plot([0.7, 0.8], [0.3, 0.3], color='green')
    plt.plot([0.8, 0.8], [0.3, 0.7], color='green')
    plt.plot([0.8, 0.7], [0.5, 0.5], color='green')

# Configuración del plot
plt.figure(figsize=(8, 4))
plt.axis('off')  # Ocultar los ejes

# Dibujar los nombres
dibujar_nombre_karen()
dibujar_nombre_diana()

# Mostrar el plot
plt.show()