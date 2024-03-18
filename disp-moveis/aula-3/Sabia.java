// implements faz parte do interface
public class Sabia extends Animal implements Bird{
    
    public Sabia(){
        super("Sabiá", 2);
    }
// implementacao do metodo abstrato falar() de animal
    public void falar(){
        System.out.println("fiu fiu fiu ");
    }

    public void voar(){ // ultimo codigo realizado para validar o interface/implements
        System.out.println("Estou voando");
    }

}

// diferenca entre abstrata e interface
// é que interface pode ter metodos implementados e interfaces nao
// interfaces so podem ter metodos abstratos