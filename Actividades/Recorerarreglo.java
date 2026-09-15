import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
       
        List<List<Integer>> matriz = new ArrayList<>();
        matriz.add(Arrays.asList(1, 2, 3, 4));
        matriz.add(Arrays.asList(5, 6, 7, 8));
        matriz.add(Arrays.asList(9, 10, 11, 12));

        
        int cantidadFilas = matriz.size();          
        int cantidadColumnas = matriz.get(0).size(); 

        System.out.println("--- RECORRIDO POR COLUMNAS ---");

        
        for (int col = 0; col < cantidadColumnas; col++) {
            System.out.println("\n--- Columna " + col + " ---");

            
            for (int fila = 0; fila < cantidadFilas; fila++) {
              
                System.out.println("Elemento en [" + fila + "][" + col + "]: " 
                        + matriz.get(fila).get(col));
            }
        }
    }
}
