package com.sl.utilidades;

import com.sl.modelos.*;

import java.util.*;
import java.util.stream.Collectors;

public class UtilidadesGeografia {


    public static List<Pais> ejercicio1(List<Pais> paises) {

        List<Pais> paisesLista = new ArrayList<>();

        for (Pais pais : paises) {
            if (pais.getComunidadesAutonomas().size() > 1 && pais.getPaisesVecinos().size() > 0) {
                paisesLista.add(pais);
            }
        }

        return new ArrayList<>(paisesLista);

    }


    public static Map<Continente, Integer> ejercicio2(List<Continente> continentes) {

        Map<Continente, Integer> continentesMap = new HashMap<>();

        for (Continente continente : continentes) {
            int cantidadPaises = continente.getPaises().size();
            continentesMap.put(continente, cantidadPaises);
        }



        return new HashMap<>(continentesMap);
    }


    public List<Ciudad> ejercicio3(List<Ciudad> ciudades, List<Pais> paises) {

        List<Ciudad> ciudadesLista = new ArrayList<>();

        Pais pais = paises.get(0);

        for (Ciudad ciudad : ciudades) {
            if (ciudad.getNombre().equals(pais.getCapital())) {

                ciudadesLista.add(ciudad);
            }


        }

        return new ArrayList<>(ciudadesLista);
    }



    public static Map<Pais, Long> ejercicio4(List<Pais> paises) {

        Map<Pais, Long> paisesMap = new HashMap<>();

        for (Pais pais : paises) {
            long totalPoblacion = 0;
            for (ComunidadAutonoma comunidadAutonoma : pais.getComunidadesAutonomas()) {
                totalPoblacion += comunidadAutonoma.getPoblacion();
            }
            paisesMap.put(pais, totalPoblacion);
        }
        return new HashMap<>(paisesMap);
    }



    public static boolean ejercicio5(InformePais informePais, Pais pais) {
        return false;
    }



    public static InformeDetalladoPais ejercicio6(Pais pais) {
        return null;
    }


}
