public abstract class Animal { // abstrata nao permite inicializar um animal generico, so serve para ser herdada.

    // protected somente se for no mesmo arquivo
    public String tipo;
    public String cor;
    public int patas;
    public double peso;
    
    public Animal(String tipo, int patas){
        System.out.println("Sou um " +tipo+ " de "+ patas+" patas!");
    }

    public abstract void falar(); // 'public abstract' ela nao é implementada, somente descrita, faz com que obrigue quem me herdar a implementa-la

}
