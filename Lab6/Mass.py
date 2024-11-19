class Mass:

    _conversion = {'mg': 0.000001,
                   'g': 0.001,
                   'kg': 1,
                   'lb': 0.453592,
                   'oz': 0.02835,
                   'stone': 6.35029}
    
    def __init__(self, value, unit = "kg"):
        self.value = value
        self.unit = unit
    
    def convert_to_kg(self):
        return self.value * Mass._conversion[self.unit]
    
    def __str__(self):
        return f"{self.convert_to_kg():.2f} kg"

    def __repr__(self):
        return f"Mass({self.value:.2f}, '{self.unit}')"