import matplotlib.pyplot as plt
import numpy as np

# Función de eficiencia en función del diámetro (ejemplo)
def calcular_eficiencia(diametro1):

    area1 = (3.14159 / 4) * (diametro1 ** 2)
    caudal=0.1
    velocidad_1 = caudal / area1
    velocidad_2 = 8.84


    return 0.001 * (860*0.1*9.81*(29.6+((1.05*((velocidad_2**2)-(velocidad_1**2)))/(2*9.81)))/1000)/22.5

# Valores de diámetro
diametros = np.linspace(0.01, 1, 1000)  # Generar 100 valores de diámetro de 0 a 1

# Calcular los valores de eficiencia correspondientes a cada diámetro
eficiencias = [calcular_eficiencia(d) for d in diametros]

# Crear la gráfica
plt.plot(diametros, eficiencias)



# Etiquetas de los ejes
plt.xlabel('Diámetro Entrada')
plt.ylabel('Eficiencia del Motor')

# Título del gráfico
plt.title('Gráfico de Diámetro Entrada vs Eficiencia del Motor')

# Mostrar la gráfica
plt.show()


