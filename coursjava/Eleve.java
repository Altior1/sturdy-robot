package coursjava;


public class Eleve {
    private final int age;
    private int classe;
    public String nom;
    public String prenom;
    Eleve(String nom,String prenom,int classe,int age){
        this.nom= nom;
        this.age=age;
        this.prenom=prenom;
        this.classe=classe;
    }
    public String getNom(){
        return this.nom;
    }
    public String getPrenom(){
        return this.prenom;
    }
    public int getAge(){
        return this.age;
    }
    public int getClasse(){
        return this.classe;
    }   
    }

