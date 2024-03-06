package compras;
// pesquisar sobre staticos
public class Produto {
    private static int contador = 0; // auto incremento
    private int id; // id de cada produto
    private String nome;
    private double valor;

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public double getValor() {
        return valor;
    }

    public Produto(String nome, double valor) {
        Produto.contador++; 
        this.id = Produto.contador;
        this.nome = nome;
        this.valor = valor;
    }

}
