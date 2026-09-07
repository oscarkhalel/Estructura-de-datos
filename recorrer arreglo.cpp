#include <iostream>
#include <vector>

int main() {
    // Matriz de 3 filas x 4 columnas usando vectores
    std::vector<std::vector<int>> matriz = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // Obtenemos las dimensiones
    int cantidadFilas = matriz.size();       // Devuelve 3
    int cantidadColumnas = matriz[0].size(); // Devuelve 4

    std::cout << "--- RECORRIDO POR COLUMNAS ---" << std::endl;

    // 1. El ciclo externo recorre las COLUMNAS
    for (int col = 0; col < cantidadColumnas; col++) {
        std::cout << "\n--- Columna " << col << " ---" << std::endl;

        // 2. El ciclo interno recorre las FILAS
        for (int fila = 0; fila < cantidadFilas; fila++) {
            // Acceso con doble corchete: [fila][columna]
            std::cout << "Elemento en [" << fila << "][" << col << "]: " 
                      << matriz[fila][col] << std::endl;
        }
    }

    return 0;
}