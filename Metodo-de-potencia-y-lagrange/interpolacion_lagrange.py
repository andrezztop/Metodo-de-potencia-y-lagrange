import numpy as np

class LagrangeInterpolator:
# Metodo __init__ especial para crear los objetos
    def __init__(self, x_puntos, y_puntos):
        self.x_puntos = np.asarray(x_puntos)
        self.y_puntos = np.asarray(y_puntos)
# Metodo de interpolación
    def interpolate(self, x_interpolate):
        y_interpolate = 0
        n = len(self.x_puntos)
        for i in range(n):
            term = self.y_puntos[i]
            for j in range(n):
                if i != j:
                    term = term * (x_interpolate - self.x_puntos[j]) / (self.x_puntos[i] - self.x_puntos[j])
            
            y_interpolate += term
        
        return y_interpolate

# Ejemplo de uso
x = np.array([1, 2, 4, 5]) 
y = np.array([3, 2, 1, 2])

lagrange = LagrangeInterpolator(x, y)
x_int = 3
y_int = lagrange.interpolate(x_int)

print(f"y({x_int}) = {y_int}")