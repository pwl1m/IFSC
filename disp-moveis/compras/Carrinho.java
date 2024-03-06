import java.util.ArrayList;
import java.util.List;

public class Carrinho {
    private List<Produto> produtos;

    public Carrinho(){
        this.produtos = new ArrayList<Produto>();
    }

    public void addProduto(Produto p){
        this.produtos.add(p);
    }

    // 
    public double calcularCompra(){
        double total = 0;
        for(Produto p: this.produtos){
            total += p.getValor();
        }
        return total;
    }

}
