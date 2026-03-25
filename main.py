from src.calculator import LogisticsCalculator

def run():
    # Ejemplo: Contenedor de 20 pies (aprox en cm) vs Caja estándar
    container = (590, 235, 239)
    box = (40, 30, 30)
    
    calc = LogisticsCalculator(container, box)
    total = calc.calculate_max_boxes()
    
    print(f"Capacidad maxima estimada: {total} unidades")
    print(f"Peso volumetrico por caja (div 5000): {calc.volumetric_weight(10)} kg")

if __name__ == "__main__":
    run()