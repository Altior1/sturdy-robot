package coursjava;


public class First{
    public static void main(String[] args) {
        System.out.println("Bonjour");
        TestEleves newTest = new TestEleves();
        String[] tab= newTest.reslutT();
        System.out.println(tab.toString());
    }
}

