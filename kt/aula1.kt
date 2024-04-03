/**
 * programa que solicita um dia um mes e informa se a data é valida
 */
fun main() {
    val dia = 27
   	val mes = 4
    
 	val diaPorMes=arrayOf(31,28,31,30,31,30,31,31,30,31,30,31)    
    val meses = arrayOf("jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez")
    
    if (dia in 1..diaPorMes[mes-1] && mes in 1..12){
        println ("dia $dia do mes de ${meses[mes-1]} é valido")
    } else{
        println ("data invalida")
    }
    
}