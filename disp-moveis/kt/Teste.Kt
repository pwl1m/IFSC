/**
 *  
 */
class Teste(val a:Int, val b:String){
	 
    fun testarMetodo():String{
        return "Hello";    
    }
}

fun main() {
	
    var t = Teste(3 , "Oi")
    println(t.a)
	println(t.testarMetodo())
}
