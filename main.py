from src.calculator import LogisticsCalculator

def run():
    # Ejemplo: Contenedor de 20 pies (590x235x239 cm)
    calc = LogisticsCalculator(590, 235, 239)
    
    # Caja de ejemplo (40x30x30 cm)
    l, w, h = 40, 30, 30
    peso_real = 12
    
    total = calc.calculate_max_boxes(l, w, h)
    peso_v = calc.get_volumetric_weight(l, w, h, peso_real)
    
    print(f"Resultado del calculo:")
    print(f"- Cajas totales: {total}")
    print(f"- Peso a cobrar (volumetrico vs real): {peso_v} kg")

if __name__ == "__main__":
    run()