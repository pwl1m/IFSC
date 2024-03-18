import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Inicio {
    public static void main(String[] args) {
        // lancamento dos produtos
        List<Produto> produtos = new ArrayList<Produto>();
        produtos.add(new Produto("teclado  ", 40.0));
        produtos.add(new Produto("mouse  ", 10.0));
        produtos.add(new Produto("pen drive  ", 5.0));
        produtos.add(new Produto("no-break  ", 400.0));
        produtos.add(new Produto("headset  ", 80.0));
        produtos.add(new Produto("mouse pad  ", 18.70));

        System.out.println(produtos.get(2));
        Scanner leitor = new Scanner(System.in);
        int opcao =1;
        Carrinho c = new Carrinho();

        while(opcao == 1){
            System.out.println("digite o id do produto ou -1 para encerrar");
            int id = leitor.nextInt();

            if(id == -1){
                break;
            }

            System.out.println("Digite a quantidade");  
            int qnt = leitor.nextInt();
            
            for(Produto p: produtos){ //pesquisar sobre for each por id
                if(p.getId() == id){ // pesquisar sobre == e equals 
                    c.addProduto(p, qnt);
                    // System.out.println("Produto adicionado no carrinho: "+p.getNome());
                    // break;
                }
            }
        }

        c.calcularCompra();
        leitor.close(); 
        // System.out.println(c.calcularCompra()); em troca da linha 34

        // outra maneira de declarar 
        // Produto p2 = new Produto("Mouse", 120.0);
        // Produto p1 = new Produto("teclado", 250.0);
        // System.out.println("Id: "+p1.getId());
        // System.out.println("Nome: "+p1.getNome());
        // System.out.println("Valor: "+p1.getValor());
        // System.out.println("Id: "+p2.getId());
        // System.out.println("Nome: "+p2.getNome());
        // System.out.println("Valor: "+p2.getValor());
    }
}