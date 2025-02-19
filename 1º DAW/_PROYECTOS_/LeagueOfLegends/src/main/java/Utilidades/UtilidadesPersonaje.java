package Utilidades;

import Modelos.Personaje;
import Modelos.Region;

import java.util.*;

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

    // Levelear un personaje y escalar sus estadisticas
    public Personaje levelMax (Personaje personaje) {

        // Realizamos un setter donde el nivel del personaje aumenta en +1
        personaje.setNombre(personaje.getNombre() + 1);

        Personaje maxPersonaje = new Personaje();

        Double ataqueBase = maxPersonaje.getAtaqueBase();
        Double defensaBase = maxPersonaje.getDefensaBase();
        Double vidaBase = maxPersonaje.getVidaBase();
        Double manaBase = maxPersonaje.getManaBase();


        ataqueBase = ataqueBase + maxPersonaje.getEscalabilidad().getIncrementoDañoNivel() * 18;
        maxPersonaje.setAtaqueBase(ataqueBase);

        defensaBase = defensaBase + maxPersonaje.getEscalabilidad().getIncrementoDefensaNivel() * 18;
        maxPersonaje.setDefensaBase(defensaBase);

        vidaBase = vidaBase + maxPersonaje.getEscalabilidad().getIncrementoSaludNivel() * 18;
        maxPersonaje.setVidaBase(vidaBase);

        manaBase = manaBase + maxPersonaje.getEscalabilidad().getIncrementoManaNivel() * 18;
        maxPersonaje.setManaBase(manaBase);

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

        Personaje maxNivelPersonaje = new Personaje();

        for (Integer nivelPersonaje = maxNivelPersonaje.getNivel(); nivelPersonaje < 18; ) {

            nivelPersonaje += 1;

            maxNivelPersonaje.setNivel(nivelPersonaje);
        }

        Double ataqueBase = maxNivelPersonaje.getAtaqueBase();
        Double defensaBase = maxNivelPersonaje.getDefensaBase();
        Double vidaBase = maxNivelPersonaje.getVidaBase();
        Double manaBase = maxNivelPersonaje.getManaBase();

        ataqueBase = ataqueBase + maxNivelPersonaje.getEscalabilidad().getIncrementoDañoNivel() * maxNivelPersonaje.getNivel();
        maxNivelPersonaje.setAtaqueBase(ataqueBase);

        defensaBase = defensaBase + maxNivelPersonaje.getEscalabilidad().getIncrementoDefensaNivel() * maxNivelPersonaje.getNivel();
        maxNivelPersonaje.setDefensaBase(defensaBase);

        vidaBase = vidaBase + maxNivelPersonaje.getEscalabilidad().getIncrementoSaludNivel() * maxNivelPersonaje.getNivel();
        maxNivelPersonaje.setVidaBase(vidaBase);

        manaBase = manaBase + maxNivelPersonaje.getEscalabilidad().getIncrementoManaNivel() * maxNivelPersonaje.getNivel();
        maxNivelPersonaje.setManaBase(manaBase);

        List<Personaje> personajeMasPoderoso = new ArrayList<>();

        personajeMasPoderoso.add(maxNivelPersonaje);

        personajeMasPoderoso.sort(Comparator.comparing(p -> p.getAtaque()+ p.getDefensa()+ p.getMana()+ p.getVida()));


        return personajeMasPoderoso.getLast();

    }

    public Map<Region, Personaje> getMasPoderosoPorRegion (List<Personaje> personajes) {
        Map<Region, List<Personaje>> nombre = getPersonajesPorRegion(personajes);
        Map<Region, Personaje> personajesMap = new HashMap<>();
        for (Region p : nombre.keySet()) {
            Personaje personaje = getMasPoderoso(nombre.get(p));
            personajesMap.put(p, personaje);
        }

        return personajesMap;
    }

}
