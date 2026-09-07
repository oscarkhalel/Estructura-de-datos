using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Matriz de 3 filas x 4 columnas usando listas
        List<List<int>> matriz = new List<List<int>>()
        {
            new List<int> { 1, 2, 3, 4 },
            new List<int> { 5, 6, 7, 8 },
            new List<int> { 9, 10, 11, 12 }
        };

        // Obtenemos las dimensiones
        int cantidadFilas = matriz.Count;          // Devuelve 3
        int cantidadColumnas = matriz[0].Count;    // Devuelve 4

        Console.WriteLine("--- RECORRIDO POR COLUMNAS ---");

        // 1. El ciclo externo recorre las COLUMNAS
        for (int col = 0; col < cantidadColumnas; col++)
        {
            Console.WriteLine($"\n--- Columna {col} ---");

            // 2. El ciclo interno recorre las FILAS
            for (int fila = 0; fila < cantidadFilas; fila++)
            {
                // Acceso con doble corchete: [fila][columna]
                Console.WriteLine($"Elemento en [{fila}][{col}]: {matriz[fila][col]}");
            }
        }
    }
}