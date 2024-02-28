public class ExOperadorLogico{

    public static void main(String[] args) {
    boolean temCartaoDeCredito = true;
    boolean temDinheiroNaConta = false;

    if (!temCartaoDeCredito && !temDinheiroNaConta){
        System.out.println("Não pode comprar");
    } 
    else {
        System.out.println("pode comprar");
    }
    }
}