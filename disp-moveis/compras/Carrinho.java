import java.util.ArrayList;
import java.util.List;

public class Carrinho {
    private List<Produto> produtos;
    private List<Integer> quantidades; // <- caso sem for
    
    public Carrinho(){
        this.produtos = new ArrayList<Produto>();
    }

    // adicionar produto e quantidade
    public void addProduto(Produto p, int qnt){
        // for(int i = 0; i < quantidade; i++){
        this.produtos.add(p);
        // }
        this.quantidades.add(qnt); // caso sem for


    }
    // primeira maneira de calcular a compra que o professor fez
    // public double calcularCompra(){
    //     double total = 0;
    //     for(Produto p: this.produtos){
    //         total += p.getValor();
    //     }
    //     return total;
    public void calcularCompra(){
        double total = 0;

        for (int i = 0; i <produtos.size(); i++){
            Produto p = produtos.get(i);
            int qnt = quantidades.get(i);
            
            System.out.println(p.getNome() + " R$ " + p.getValor()+ "x" +qnt);
            total += p.getValor()*qnt;
        }
        System.out.println("total da compra" +total);
    }
}