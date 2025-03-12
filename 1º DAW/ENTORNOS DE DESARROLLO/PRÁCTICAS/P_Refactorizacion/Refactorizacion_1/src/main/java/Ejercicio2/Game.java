package Ejercicio2;

public class Game {

    Player p;

    public void movement(String m) {
        if (m.equalsIgnoreCase("Derecha")) {
            p.setX(p.getx() + 1);

            if (m.equalsIgnoreCase("Izquierda")) {
                p.setX(p.getx() - 1);

                if (m.equalsIgnoreCase("Arriba")) {
                    p.setY(p.gety() - 1);
                    if
                    (m.equalsIgnoreCase("Abajo")){
                        p.setY(p.gety() + 1);
                    }
                }
            }
        }
    }


    public Game(Player p) {
        this.p = p;
    }
}
