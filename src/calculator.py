class LogisticsCalculator:
    def __init__(self, container_dims, box_dims):
        """
        dims: (largo, ancho, alto) en cm
        """
        self.c_l, self.c_w, self.c_h = container_dims
        self.b_l, self.b_w, self.b_h = box_dims

    def calculate_max_boxes(self):
        # Calcula orientación estándar (sin rotación compleja)
        fit_l = self.c_l // self.b_l
        fit_w = self.c_w // self.b_w
        fit_h = self.c_h // self.b_h
        
        total_boxes = fit_l * fit_w * fit_h
        return int(total_boxes)

    def volumetric_weight(self, weight_kg, divisor=5000):
        # Estándar internacional para carga aérea/terrestre
        volume = (self.b_l * self.b_w * self.b_h) / divisor
        return max(weight_kg, volume)