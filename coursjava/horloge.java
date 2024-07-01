package coursjava;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.processing.Generated;

public class horloge {
    int heure=0;
    int minute=0;
    int seconde=0;
    public horloge(int h,int m, int s){
        this.heure=h;
        this.minute=m;
        this.seconde=s;
    }
    public void setHoraire(int h,int m,int s){
        this.heure=h;
        this.minute=m;
        this.seconde=s;
    }
    public Map<String, Integer> getHoraire(){
        Map <String,Integer> horaire = new HashMap<String,Integer>();
        horaire.putAll(('heure',this.heure),('minute',this.minute),('seconde',this.seconde));
        return horaire;
    }
}

