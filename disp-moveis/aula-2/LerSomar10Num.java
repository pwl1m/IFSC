import java.util.Scanner;

// Faça um programa que leia 10 números 
// colocando-os em um array. Em seguida exiba a 
// soma de todos este números

public class LerSomar10Num{
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in); // scanner para ler numeros

    double[] numeros = new double[10]; // criando array tipo double 64b = float 32b

    System.out.println("Digite 10 números:");

    for (int i = 0; i < 10; i++) {
            System.out.print("Número " + (i + 1) + ": "); // i+1 para começar do 1 
        numeros[i] = scanner.nextDouble(); // lê o número digitado e armazena no array
    }
    scanner.close(); // fecha o scanner após a leitura dos números

    double soma = 0; // inicia a variável soma com 0

    for (int i = 0; i < 10; i++) { // loop para somar os números
        soma += numeros[i]; // soma o número atual ao valor acumulado
    }
        
    System.out.println("A soma dos números é: " + soma);
}
}
