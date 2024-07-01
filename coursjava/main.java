package coursjava;
import java.util.Scanner;
import java.util.Map;



public class main {
    public static void main(String[] args) {
        String value;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("combien de cellule ? :");
            int nbTour = sc.nextInt()+1;
            String table[] = new String[nbTour];
            for(int i=0;i<nbTour;i++){
                System.out.println("quel nouvel ajout ?: ");
                value=sc.nextLine();
                table[i]=value;
            }}
        catch(){

        }
    }
}
