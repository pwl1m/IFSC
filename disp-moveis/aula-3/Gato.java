public final class Gato extends Animal{ // extends para importar o Animal
    // FINAL no lugar de class garante que não pode ser herdada
    public Gato(){
        super("gato",4);
    }

    public void falar(){
        System.out.println("miaumimi");
    }

}
