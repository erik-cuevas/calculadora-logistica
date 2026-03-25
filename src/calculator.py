class LogisticsCalculator:
    def __init__(self, c_l, c_w, c_h):
        # Dimensiones del contenedor (Largo, Ancho, Alto)
        self.container = (c_l, c_w, c_h)

    def calculate_max_boxes(self, b_l, b_w, b_h):
        # Validacion: dimensiones deben ser mayores a cero
        if any(d <= 0 for d in self.container + (b_l, b_w, b_h)):
            return 0
        
        # Calculo de cuantas cajas caben por cada eje
        fit_l = self.container[0] // b_l
        fit_w = self.container[1] // b_w
        fit_h = self.container[2] // b_h
        
        return int(fit_l * fit_w * fit_h)

    def get_volumetric_weight(self, l, w, h, weight_kg, divisor=5000):
        # Formula estandar de la industria logistica
        vol_weight = (l * w * h) / divisor
        return max(weight_kg, vol_weight)