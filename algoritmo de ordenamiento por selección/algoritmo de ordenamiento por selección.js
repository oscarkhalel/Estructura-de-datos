    let n = a.length;
    for (let i = 0; i < n; i++) {
        let small = i;
        for (let j = i + 1; j < n; j++) {
            if (a[small] > a[j]) {
                small = j;
            }
        }
        // Intercambio mediante desestructuración
        [a[i], a[small]] = [a[small], a[i]];
    }
}

function printArr(a) {
    let result = "";
    for (let i = 0; i < a.length; i++) {
        result += a[i] + " ";
    }
    process.stdout.write(result);
}

let a = [65, 26, 13, 23, 12];

console.log("Arreglo antes de ser ordenado: ");
printArr(a);

selection(a);

console.log("\nArreglo despues de ser ordenado: ");
printArr(a);
