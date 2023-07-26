def calcular_eficiencia_bomba(caudal, diametro1, diametro2, emotor, consumo_e, diferencia_presion, viscosidad_cin, gravedad, densidad):
    # Cálculo de la velocidad en los dos puntos
    area1 = (3.14159 / 4) * (diametro1 ** 2)
    area2 = (3.14159 / 4) * (diametro2 ** 2)
    velocidad_1 = caudal / area1
    velocidad_2 = caudal / area2

    # Cálculo de Re1 y Re2
    Re1 = (diametro1 * velocidad_1 * densidad) / viscosidad_cin
    Re2 = (diametro2 * velocidad_2 * densidad) / viscosidad_cin

    # Verificar si Re1 o Re2 son mayores o iguales a 4000
    if Re1 >= 4000 or Re2 >= 4000:
        alfa = 1.05
    # Verificar si Re1 o Re2 son menores o iguales a 2300
    elif Re1 <= 2300 and Re2 <= 2300:
        alfa = 2
    else:
        alfa = 1.0  # Valor predeterminado si no se cumple ninguna condición

    # Cálculo de la energía cinética en los dos puntos
    hbomba = (diferencia_presion / (densidad * gravedad)) + (alfa * ((velocidad_2 ** 2) - (velocidad_1 ** 2)) / (2 * gravedad))

    # Cálculo de la energía potencial en los dos puntos
    wbomba = densidad * caudal * gravedad * hbomba
    wbomba_eje = emotor * consumo_e

    # Cálculo de la eficiencia
    eficiencia = wbomba / wbomba_eje

    return eficiencia


# Datos de entrada
caudal = 0.1  # en m^3/s
diametro1 = 0.08  # en metros
diametro2= 0.12
diferencia_presion = 250000  # en Pa
emotor= 0.9
consumo_e= 25000
viscosidad_cin= 1
gravedad = 9.81  # en m/s^2
densidad = 860  # en kg/m^3

# Llamada a la función para calcular la eficiencia
eficiencia = calcular_eficiencia_bomba(caudal,diametro1, diametro2,emotor,consumo_e,diferencia_presion, viscosidad_cin,gravedad, densidad)

# Imprimir el resultado
print(f"La eficiencia de la bomba es: {eficiencia}")