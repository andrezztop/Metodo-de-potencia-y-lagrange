#inicio del programa
# autores: gustavo paez, victor marcano, andres chavez
import numpy as np

class MetodoPotencia:
    def metodo_potencia(self, matriz, iteraciones):
        # Metodo de la potencia
        vector = self.crear_vector()
        vector = vector / np.linalg.norm(vector)

        for _ in range(iteraciones):
            vector = self.multiplica(matriz, vector)
            vector = vector / np.linalg.norm(vector)

        eigenvalor = np.dot(vector, np.dot(matriz, vector))

        return eigenvalor, vector

    def crear_vector(self):
        # Crea un vector aleatorio de tamano 5
        return np.random.rand(5)

    def crear_matriz_c(self, n):
        # Crea una matriz cuadrada n
        return np.random.rand(n, n)

    def multiplica(self, matriz, vector):
        # Metodo que multiplica la matriz por el vector
        return np.dot(matriz, vector)

if __name__ == "__main__":
    n = 5
    matriz = MetodoPotencia().crear_matriz_c(n)
    iteraciones = 100
    eigenvalor, eigenvector = MetodoPotencia().metodo_potencia(matriz, iteraciones)
    print(f"eigenvalor dominante: {eigenvalor:.4f}")
    print(f"eigenvector dominante: \n{eigenvector}")
# fin del programa 
