using System;

class Program {
    static void Selection(int[] a) {
        int n = a.Length;
        for (int i = 0; i < n; i++) {
            int small = i;
            for (int j = i + 1; j < n; j++) {
                if (a[small] > a[j]) {
                    small = j;
                }
            }
            // Intercambio equivalente a a[i], a[small] = a[small], a[i]
            int temp = a[i];
            a[i] = a[small];
            a[small] = temp;
        }
    }

    static void PrintArr(int[] a) {
        for (int i = 0; i < a.Length; i++) {
            Console.Write(a[i] + " ");
        }
    }

    static void Main() {
        int[] a = { 65, 26, 13, 23, 12 };

        Console.Write("Arreglo antes de ser ordenado: ");
        PrintArr(a);

        Selection(a);

        Console.Write("\nArreglo despues de ser ordenado: ");
        PrintArr(a);
    }
}
