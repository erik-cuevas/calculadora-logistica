# Calculadora de Cubicaje Logistico

Esta aplicacion desarrollada en Python esta diseñada para la optimizacion de procesos logisticos. Permite determinar la capacidad maxima de carga de un contenedor segun dimensiones especificas y calcular el peso volumetrico para envíos de carga.

## Funcionalidades Principales

- Calculo de Capacidad: Determina la cantidad de unidades que caben en un contenedor segun sus dimensiones (Largo, Ancho, Alto).
- Peso Volumetrico: Compara el peso real frente al peso volumetrico basado en el divisor estandar industrial (5000) para determinar el peso facturable.
- Validacion de Datos: El sistema integra validaciones para asegurar que las dimensiones ingresadas sean superiores a cero, evitando errores en el calculo.

## Estructura del Proyecto

- src/: Contiene la logica principal de la aplicacion (calculator.py).
- tests/: Incluye pruebas unitarias para asegurar la precision de los resultados.
- main.py: Punto de entrada para ejecutar ejemplos de uso.

## Instalacion y Ejecucion

1. Clonar el repositorio:
   git clone https://github.com/erik-cuevas/calculadora-logistica

2. Navegar al directorio del proyecto:
   cd calculadora-logistica

3. Ejecutar la aplicacion:
   python main.py

4. Ejecutar las pruebas unitarias:
   python -m unittest tests/test_calculator.py

## Ejemplo de Implementacion

```python
from src.calculator import LogisticsCalculator

# Instancia con dimensiones de un contenedor de 20 pies (cm)
calc = LogisticsCalculator(590, 235, 239)

# Calculo de capacidad para cajas de 40x30x30 cm
total = calc.calculate_max_boxes(40, 30, 30)
print(f"Capacidad estimada: {total} unidades")
```
