import matplotlib.pyplot as plt
import numpy as np

def calcular_eficiencia_bomba(caudal,diametro1,alfa1, diametro2,emotor,consumo_e,diferencia_presion, viscosidad_cin,gravedad, densidad):

    # Cálculo de la velocidad en los dos puntos
    area1 = (3.14159 / 4) * (diametro1 ** 2)
    area2 = (3.14159 / 4) * (diametro2 ** 2)

    velocidad_1 = caudal / area1
    velocidad_2 = caudal / area2


    if viscosidad_cin is None:

        alfa=alfa1

        # Cálculo de la energía cinética en los dos puntos
        hbomba = (diferencia_presion / (densidad * gravedad)) + (alfa * ((velocidad_2 ** 2) - (velocidad_1 ** 2)) / (2 * gravedad))

        # Cálculo de la energía potencial en los dos puntos
        wbomba = (densidad * caudal * gravedad * hbomba)

        wbomba_eje = emotor * consumo_e

        # Cálculo de la eficiencia
        eficiencia = wbomba / wbomba_eje

        return eficiencia
    else:
        alfa=1.05
        # Cálculo de Re1 y Re2
        Re1 = (diametro1 * velocidad_1) / viscosidad_cin
        Re2 = (diametro2 * velocidad_2) / viscosidad_cin

        print(Re1)
        print(Re2)

        # Verificar si Re1 o Re2 son mayores o iguales a 4000
        if Re1 >= 4000 or Re2 >= 4000:
            alfa = 1.05
        # Verificar si Re1 o Re2 son menores o iguales a 2300
        elif Re1 <= 2300 or Re2 <= 2300:
            alfa = 2
        print(alfa)
        # Cálculo de la energía cinética en los dos puntos
        hbomba = (diferencia_presion / (densidad * gravedad)) + (
                    alfa * ((velocidad_2 ** 2) - (velocidad_1 ** 2)) / (2 * gravedad))

        # Cálculo de la energía potencial en los dos puntos
        wbomba = (densidad * caudal * gravedad * hbomba)

        wbomba_eje = emotor * consumo_e

        # Cálculo de la eficiencia
        eficiencia = wbomba / wbomba_eje

        return eficiencia


# Datos de entrada
caudal = 0.1  # en m^3/s
diametro1 = 0.08  # en metros
diametro2= 0.12  # en metros
diferencia_presion = 250000  # en Pa
emotor= 0.9
consumo_e= 25000 # en W
alfa1= 1.05
viscosidad_cin= None # en m^2/s
gravedad = 9.81  # en m/s^2
densidad = 860  # en kg/m^3

# Llamada a la función para calcular la eficiencia
eficiencia = calcular_eficiencia_bomba(caudal,diametro1, alfa1,diametro2,emotor,consumo_e,diferencia_presion, viscosidad_cin,gravedad, densidad)

# Imprimir el resultado
print(f"La eficiencia de la bomba es: {eficiencia}")

# Función de eficiencia en función del diámetro (ejemplo)
def calcular_eficiencia(diametro):
    # Tu función de eficiencia en función del diámetro aquí
    return 0.9 - 0.1 * diametro

# Valores de diámetro
diametros = np.linspace(0, 10, 100)  # Generar 100 valores de diámetro de 0 a 10

# Calcular los valores de eficiencia correspondientes a cada diámetro
eficiencias = [calcular_eficiencia(d) for d in diametros]

# Crear la gráfica
plt.plot(diametros, eficiencias)

# Etiquetas de los ejes
plt.xlabel('Diámetro')
plt.ylabel('Eficiencia del Motor')

# Título del gráfico
plt.title('Gráfico de Diámetro vs Eficiencia del Motor')

# Mostrar la gráfica
plt.show()
