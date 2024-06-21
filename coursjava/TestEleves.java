package coursjava;


public class TestEleves {
    @Override
    public String toString() {
        return "TestEleves []";
    }
    TestEleves() {
        for(int i=0;i<5;i++){
            Eleve test = new Eleve("test","test2",i,i+10);
            System.out.println(test.getAge());
        }
    }
}
