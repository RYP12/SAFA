package Utilidades;

import Modelos.Item;
import Modelos.Personaje;

import java.awt.*;
import java.util.List;

public class UtilidadesItem {

    public void equiparItem (Personaje personaje, Item item) {

        List<Item> items = personaje.getEquipamiento();
        items.add(item);
        personaje.setEquipamiento(items);

        personaje.setAtaque(item.getAumentoDaño() + personaje.getAtaque());
        personaje.setDefensa(item.getAumentoDefensa() + personaje.getDefensa());
        personaje.setMana(item.getAumentoMana() + personaje.getMana());
        personaje.setVida(item.getAumentoSalud() + personaje.getVida());

    }

}
