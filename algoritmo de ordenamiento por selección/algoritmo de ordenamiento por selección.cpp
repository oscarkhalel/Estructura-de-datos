#include <iostream>
#include <vector>
#include <algorithm> // Para std::swap

void selection(std::vector<int>& a) {
    int n = a.size();
    for (int i = 0; i < n; i++) {
        int small = i;
        for (int j = i + 1; j < n; j++) {
            if (a[small] > a[j]) {
                small = j;
            }
        }
        std::swap(a[i], a[small]);
    }
}

void printArr(const std::vector<int>& a) {
    for (int i = 0; i < a.size(); i++) {
        std::cout << a[i] << " ";
    }
}

int main() {
    std::vector<int> a = {65, 26, 13, 23, 12};

    std::cout << "Arreglo antes de ser ordenado: ";
    printArr(a);

    selection(a);

    std::cout << "\nArreglo despues de ser ordenado: ";
    printArr(a);

    return 0;
}
