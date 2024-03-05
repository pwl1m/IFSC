import java.util.Scanner;

// Desenvolva um programa que leia 10 números 
// colocando-os em um array A. Em seguida transfira 
// para outro array B os valores contidos no array A 
// em ordem inversa

public class ArrayInverter{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] arrayA = new int[10];
        int[] arrayB = new int[10];

        System.out.println("digite 10 números:");

        for (int i=0 ; i<10; i++) {
            System.out.print("número " + (i + 1) + ": ");
            arrayA[i] = scanner.nextInt();
        }
        scanner.close();

        // transferir de A para B em ordem inversa
        for (int i=0 ; i<10; i++) {
            arrayB[i] = arrayA[9 - i]; // 9 - i para inverter a ordem dos valores, exemplo: 9 - 0 = 9, 9 - 1 = 8, 9 - 2 = 7...
        }

        System.out.println("valores do array B (inverso de A):");
        for (int i=0 ; i<10 ; i++) {
            System.out.print(arrayB[i] + " ");
        }
    }
}
