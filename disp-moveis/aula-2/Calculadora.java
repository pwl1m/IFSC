import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {

        Scanner leitor= new Scanner(System.in);
        System.out.println("digite dois numeros inteiros");
        int a = leitor.nextInt();
        int b = leitor.nextInt();
        leitor.close();

        Dividir d = new Dividir();
        // double resultado = d.resultado(a, b);
        System.out.println("resultado: " + d.resultado(a,b));
    }
}