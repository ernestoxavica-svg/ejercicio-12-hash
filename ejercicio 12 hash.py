class TablaHashEstudiantes:
    """Tabla hash sencilla con manejo de colisiones mediante encadenamiento."""

    def __init__(self, tamano=10):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def _funcion_hash(self, matricula):
        """Calcula el índice a partir de la suma ASCII de los caracteres de la matrícula."""
        suma_ascii = sum(ord(caracter) for caracter in matricula.upper())
        return suma_ascii % self.tamano

    def insertar(self, matricula, datos_estudiante):
        indice = self._funcion_hash(matricula)
        for par in self.tabla[indice]:
            if par[0].upper() == matricula.upper():
                par[1] = datos_estudiante
                return
        self.tabla[indice].append([matricula.upper(), datos_estudiante])

    def buscar(self, matricula):
        indice = self._funcion_hash(matricula)
        comparaciones = 0
        for clave, valor in self.tabla[indice]:
            comparaciones += 1
            if clave == matricula.upper():
                return indice, valor, comparaciones
        return indice, None, comparaciones


def ejecutar_hash():
    tabla_estudiantes = TablaHashEstudiantes(tamano=11)
    registros = {
        "MAT202601": {"nombre": "Ana Sofía Gómez", "carrera": "Ing. en Software", "promedio": 9.4},
        "MAT202602": {"nombre": "Luis Fernando Pérez", "carrera": "Ciencias de Datos", "promedio": 8.9},
        "MAT202603": {"nombre": "Valeria Morales", "carrera": "Ing. en Software", "promedio": 9.7},
        "MAT202604": {"nombre": "Carlos Alberto Ruiz", "carrera": "Sistemas Computacionales", "promedio": 8.5},
    }

    for matricula, datos in registros.items():
        tabla_estudiantes.insertar(matricula, datos)

    print("\n--- EJERCICIO 3: BÚSQUEDA HASH (MATRÍCULAS ESTUDIANTILES) ---")
    print("Matrículas disponibles de ejemplo:", ", ".join(registros.keys()))
    matricula_buscada = input("Ingresa la matrícula a consultar: ").strip()

    bucket, estudiante, comparaciones = tabla_estudiantes.buscar(matricula_buscada)

    print(f"Bucket (índice hash) calculado: {bucket}")
    if estudiante:
        print(
            f"Estudiante: {estudiante['nombre']} | "
            f"Carrera: {estudiante['carrera']} | "
            f"Promedio: {estudiante['promedio']}"
        )
    else:
        print("No se encontró ningún estudiante con esa matrícula.")
    print(f"Comparaciones dentro del bucket: {comparaciones}")


if __name__ == "__main__":
    ejecutar_hash()