import java.util.ArrayList;
import java.util.List;

public class Disciplina{
    private int ch;
    private String nome;
    private List<Aluno> alunos = new ArrayList<>();
    private Professor prof;

    public Disciplina (int ch, String nome){
        if(ch<=0 || ch>200){
            throw new IllegalArgumentException("CH invalida");
        }
        this.ch=ch;
        this.nome=nome;
    }

    public void addAluno(Aluno a){
        alunos.add(a);
    }
    
    public void listarAlunos(){
        for(Aluno aluno : aluno){
        System.out.println(aluno.getNome());
    }
    }
    
    public Professor get.Professor(){
        return this.prof;
    }
    
}
