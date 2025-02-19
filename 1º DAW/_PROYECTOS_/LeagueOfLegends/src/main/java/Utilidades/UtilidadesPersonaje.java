package Utilidades;

import Modelos.Personaje;
import Modelos.Region;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UtilidadesPersonaje {

    // Levelear un personaje y escalar sus estadisticas
    public Personaje levelUp (Personaje personaje) {

        // Realizamos un setter donde el nivel del personaje aumenta en +1
        personaje.setNombre(personaje.getNombre() + 1);

        Personaje newPersonaje = new Personaje();

        Double ataqueBase = newPersonaje.getAtaqueBase();
        Double defensaBase = newPersonaje.getDefensaBase();
        Double vidaBase = newPersonaje.getVidaBase();
        Double manaBase = newPersonaje.getManaBase();


        ataqueBase = ataqueBase + newPersonaje.getEscalabilidad().getIncrementoDañoNivel() * newPersonaje.getNivel();
        newPersonaje.setAtaqueBase(ataqueBase);

        defensaBase = defensaBase + newPersonaje.getEscalabilidad().getIncrementoDefensaNivel() * newPersonaje.getNivel();
        newPersonaje.setDefensaBase(defensaBase);

        vidaBase = vidaBase + newPersonaje.getEscalabilidad().getIncrementoSaludNivel() * newPersonaje.getNivel();
        newPersonaje.setVidaBase(vidaBase);

        manaBase = manaBase + newPersonaje.getEscalabilidad().getIncrementoManaNivel() * newPersonaje.getNivel();
        newPersonaje.setManaBase(manaBase);

        return personaje;
    }

    // Biblioteca de peronajes segun su region
    public Map<Region, List<Personaje>> getPersonajesPorRegion (List<Personaje> personajes) {
        Map<Region, List<Personaje>> personajesPorRegion = new HashMap<>();

        for (Personaje personaje : personajes) {
                // Si en el mapa el personaje no tiene region
            if (!personajesPorRegion.containsKey(personaje.getRegion())) {

                // Si la región no está en el mapa, crear una nueva entrada
                personajesPorRegion.put(personaje.getRegion(),new ArrayList<>(List.of(personaje)));

            }
            else {
                // Si la región ya está en el mapa, agregar el personaje a la lista existente
                personajesPorRegion.get(personaje.getRegion()).add(personaje);
            }
        }
        return personajesPorRegion;
    }

    public Personaje getMasPoderoso (List<Personaje> personajes) {

    }


}
