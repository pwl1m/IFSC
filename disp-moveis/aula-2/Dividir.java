public class Dividir {
    public Dividir(){
        System.out.println("novo obj Dividir");
    }

    public double resultado(int a, int b) {
        try{
            double resultado = a/b;
            return resultado;
        } catch(Exception e){
            System.out.println("não foi possivel realizar a divisao");
            return 0;
        }
    }
}
