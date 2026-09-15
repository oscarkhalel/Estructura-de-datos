// Matriz de 3 filas x 4 columnas usando arrays
const matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
];

// Obtenemos las dimensiones
const cantidadFilas = matriz.length;          // Devuelve 3
const cantidadColumnas = matriz[0].length;    // Devuelve 4

console.log("--- RECORRIDO POR COLUMNAS ---");

// 1. El ciclo externo recorre las COLUMNAS
for (let col = 0; col < cantidadColumnas; col++) {
    console.log(`\n--- Columna ${col} ---`);

    // 2. El ciclo interno recorre las FILAS
    for (let fila = 0; fila < cantidadFilas; fila++) {
        // Acceso con doble corchete: [fila][columna]
        console.log(`Elemento en [${fila}][${col}]: ${matriz[fila][col]}`);
    }
}
