import java.util.ArrayList;


public class Aluno extends Pessoa{
    private int num_matricula;
    private List<Disciplina> disciplinas = new ArrayList<>();

    public Aluno (String nome,int num_matricula){
        super(nome);
        this.num_matricula = num_matricula;
    }

    // não utilizamos
    public List<Disciplina> getDisciplina(){
        return this.disciplinas;
    }
}
