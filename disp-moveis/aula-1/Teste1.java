import java.util.Scanner;

public class Teste1 {
    public static void main(String[] args) {
        String nome = "Maria"; // variavel mas e implementado por uma class e se comporta tbm como objeto 
        int idade = 20; // variavel primitiva
        String nome2 ="Ana";
        int idade2 = 22;
        
        // comparação de strings com java
        if(nome.equalsIgnoreCase(nome2)){
            System.out.println("São nomes iguais");
            }
        else{
            System.out.println("São nomes diferentes");
        }

        // comparacao de tipos primitivos
        if (idade==idade2){
            System.out.println("São nomes iguais");
            }
        else{
            System.out.println("São nomes diferentes");
        }

        // concatenação
        System.out.println(nome+" possui "+idade+" anos ");

        // entrada de dados
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite um numero: ");

        int x = leitor.nextInt();
        System.out.println("Voçê digitou "+x);
    }    
}