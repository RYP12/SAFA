package Utilidades;

import Modelos.Habilidad;
import Modelos.Item;
import Modelos.Personaje;

public class UtilidadesHabilidad {

    public void golpearConHabilidad(Personaje emisor, Personaje receptor, Habilidad habilidadEmisor) {

        UtilidadesPersonaje maxLevel = new UtilidadesPersonaje();

        UtilidadesItem uItem = new UtilidadesItem();

        Personaje p1 = maxLevel.levelMax(emisor);
        Personaje p2 = maxLevel.levelMax(receptor);

        if (!(emisor.getEquipamiento() == null && emisor.getEquipamiento().isEmpty())){
            for (Item i : emisor.getEquipamiento()){
                uItem.equiparItem(emisor, i);
            }
        }

        if (!(receptor.getEquipamiento() == null && receptor.getEquipamiento().isEmpty())){
            for (Item i : receptor.getEquipamiento()){
                uItem.equiparItem(emisor, i);
            }
        }

        Double dañoHabilidad = habilidadEmisor.getDañoBase() + (0.2 * emisor.getAtaque() - (0.1 * receptor.getDefensa()));

        emisor.setMana(emisor.getMana() - habilidadEmisor.getCosteMana());
        receptor.setVida(receptor.getVida() - dañoHabilidad);

    }



}
