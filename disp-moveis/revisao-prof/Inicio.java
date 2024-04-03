
public class Inicio {

    public static void main(String[] args) {
        try{
            Aluno a1 = new Aluno("Aluno", 123);
            Aluno a2 = new Aluno("Aluna", 456);
            Aluno a3 = new Aluno("Aluni", 789);

            Professor p = new Professor("Miguel", 1);
            Disciplina d = new Disciplina("info", 30);

            p.setProfessor(p);
            d.addAluno(a3);
            d.addAluno(a2);
            d.addAluno(a1);

            System.out.println("");
            d.listarAlunos();
            System.out.println("");
            System.out.println(d.getProfessor);

        } catch (Exception e){

        }
    }

}
