import java.util.Scanner;

public class Aposentadoria{
// informar se a pessoa pode ou nao aposentar
// ler idade sexo e o tempo de serviço
// homens > 65 anos e ter trabalhado 30 a
// mulher > 60 anos e ter trabalhado 25 a

    public static void main(String[] args) {
        Scanner user = new Scanner(System.in);
        
        System.out.println("Nome");
        String nome = user.nextLine(); 
        
        System.out.println("digite o sexo");
        String sexo = user.nextLine(); 
        // user.next().charAt(0); // o next le a palavra, o charAt pega a primeira letra
        
        System.out.println("tempo de servico");
        int tempo = user.nextInt();  // ler entrada do usuario

        System.out.println("idade");
        int idade = user.nextInt();  // ler entrada do usuario

        System.out.println("nome é: "+nome+ " sexo: "+sexo+" tempo de servico "+tempo+" e sua idade: "+idade);  // saída

        if (sexo.equals("m") && idade >= 65 && tempo >= 30){
            System.out.println("pode aposentar");
        } else if (sexo.equals("f") && idade >= 60 && tempo >= 25){
            System.out.println("pode aposentar");
        } else {
            System.out.println("nao pode aposentar");
        }

        
    }
}
