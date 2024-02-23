def calcular_resistencia(pt100_temperatura):
    resistencia_0 = 100.0
    coeficiente_temperatura = 0.00385

    resistencia = resistencia_0 * (1 + coeficiente_temperatura * pt100_temperatura)
    return resistencia

temperatura = 30.0
resistencia_calculada = calcular_resistencia(temperatura)
print('VALORES INICIALES:\nResistencia 0 °C = 100.0 \nCoeficiente de temperatura = 0.00385')
print("Resistencia a", temperatura, "grados °C:", resistencia_calculada)