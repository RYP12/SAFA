import java.util.ArrayList;
import java.util.List;

public class Equipo implements Poderes, Mostrable {

    private String nombreEquipo;
    private List<PersonajeMarvel> miembros;

    public Equipo(String nombreEquipo) {
        this.nombreEquipo = nombreEquipo;
        this.miembros = new ArrayList<PersonajeMarvel>();
    }


    public void agregarMiembro(PersonajeMarvel nuevoMiembro) {
        miembros.add(nuevoMiembro);
    }

    public void quitarMiembro(PersonajeMarvel miembro) {
        miembros.remove(miembro);
    }


    @Override
    public double obtenerPoder() {
        double sumaPoder = 0;
        for (PersonajeMarvel personaje : miembros) {
            sumaPoder += personaje.obtenerPoder();
        }
        return miembros.isEmpty() ? 0 : sumaPoder / miembros.size();
    }



    @Override
    public String mostrarInformacion() {
        return "Equipo" +
                nombreEquipo + '\'' +
                ", miembros:" + miembros +
                '.';
    }
}