package Utilidades;

import Modelos.Pokemon;
import Modelos.TipoAtaque;
import Modelos.TipoPokemon;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class UtilidadesPokemon {

    public List<Pokemon> obtenerPokemonConTipos (List<Pokemon> pokemons, List<TipoPokemon> tipos){
        List<Pokemon> solucion = new ArrayList<>();

        for (Pokemon p : pokemons) {

            List<TipoPokemon> tipoPokemons = new ArrayList<>(p.getTipos());

            //RETAINALL

            if (tipoPokemons.retainAll(tipos)){
                solucion.add(p);
            }
        }


        return solucion;
    }

    public Map<TipoPokemon, List<Pokemon>> obtenerPokemonsPurosPorTipo(List<Pokemon> pokemons){

        Map<TipoPokemon, List<Pokemon>> mapa = new HashMap<>();
        for (Pokemon p : pokemons) {

            if (p.getTipos().size() == 1){
                if (mapa.containsKey(p.getTipos().get(0))){
                    mapa.get(p.getTipos().get(0)).add(p);

            }
        }


        return mapa;
    }


















}
