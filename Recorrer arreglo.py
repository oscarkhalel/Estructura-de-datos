       
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Obtenemos las dimensiones
cantidad_filas = len(matriz)          # Devuelve 3
cantidad_columnas = len(matriz[0])     # Devuelve 4

print("--- RECORRIDO POR COLUMNAS ---")

# 1. El ciclo externo recorre las COLUMNAS
for col in range(cantidad_columnas):
    print(f"\n--- Columna {col} ---")
    
    # 2. El ciclo interno recorre las FILAS
    for fila in range(cantidad_filas):
        # En Python las matrices tipo lista se acceden como [fila][columna]
        print(f"Elemento en [{fila}][{col}]: {matriz[fila][col]}")