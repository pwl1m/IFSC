/**
 * criar uma calculadora 
 */
import kotlin.math.pow

fun main() {
	println( calcular(2.0,3.0, potencia ))
	println( calcular(2.0,3.0, ::somar ))
	println( calcular(2.0,3.0, ::subtrair ))
}

//somar    
fun somar (a:Double,b:Double):Double{
    return a+b
}

//subtrair
fun subtrair(a:Double,b:Double) = a-b
    
//multiplicar
fun multiplicar(a:Double,b:Double) = a*b

//dividir
fun dividir(a:Double,b:Double) = a/b

//potencia
val potencia={ a:Double, b:Double -> a.pow(b) }

//calcular
fun calcular ( a:Double, b:Double, f:(Double,Double ) -> Double ) = f(a,b)