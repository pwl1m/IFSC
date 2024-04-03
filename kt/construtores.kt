/**
 *  
 */
class Curso(val nome:String, ch:Int, val modalidade:String){
	 
    val turno = "noturno"
    var cargaHoraria = 0
    
    init {
		if (ch>0){
            cargaHoraria=ch
        }else{
            println("carga horaria invalida")
        }
    }

	constructor(nome:String):this(nome, 0, "ead"){
		
	}

	constructor():this("qualquer nome",4,"local")

}

fun main() {
	
	val c = Curso("CSTSI", 3000, "Presencial")
    val c2 = Curso ("Outro Curso")
	val c3 = Curso()
    
	println("${c.nome} carha horaria ${c.cargaHoraria} ${c.modalidade}")
    println("${c2.nome} carha horaria ${c2.cargaHoraria} ${c2.modalidade}")
    println("${c3.nome} carha horaria ${c3.cargaHoraria} ${c3.modalidade}")
}