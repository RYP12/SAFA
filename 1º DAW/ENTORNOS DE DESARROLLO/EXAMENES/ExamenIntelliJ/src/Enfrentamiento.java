import java.util.Random;

public class Enfrentamiento {

    private Poderes equipo1;
    private Poderes equipo2;


    public Enfrentamiento(Poderes equipo1, Poderes equipo2) {
        this.equipo1 = equipo1;
        this.equipo2 = equipo2;
    }


    public String simularEnfrentamiento() {
        Random random = new Random();
        double factor1 = 1.0 + (2.0 - 1.0) * random.nextDouble();
        double factor2 = 1.0 + (2.0 - 1.0) * random.nextDouble();

        double poderEquipo1 = equipo1.obtenerPoder() * factor1;
        double poderEquipo2 = equipo2.obtenerPoder() * factor2;



        if (poderEquipo1 > poderEquipo2) {
            return "El equipo ganador es: " + ((Mostrable) equipo1).mostrarInformacion();
        } else if (poderEquipo2 > poderEquipo1) {
            return "El equipo ganador es: " + ((Mostrable) equipo2).mostrarInformacion();
        } else {
            return "El enfrentamiento terminó en empate.";
        }
    }
}