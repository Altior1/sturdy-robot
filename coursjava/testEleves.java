package coursjava;


public class TestEleves {
    // création des élèves pour tester les méthodes
    Eleve [] batterieTest = new Eleve[5];

    @Override
    public String toString() {
        return "TestEleves []";
    }
    TestEleves() {
        for(int i=0;i<5;i++){
            Eleve test = new Eleve("test","test2",i,i+10);
            batterieTest[i]=test;
        }
    }
    public String[] reslutT(){
        String[] tab = new String[5];
        for(int i=0;i<5;i++){
            Eleve eleve=this.batterieTest[i];
            tab[i]=eleve.toString();
        }
        return tab;
    }
}
