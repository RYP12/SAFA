public class Main {
    public static void main(String[] args) {
        PersonajeMarvel spiderMan = new PersonajeMarvel(
                "Peter Parker",
                "Spider-Man",
                true,
                "sentido aracnido",
                "Avengers",
                8.5);
        PersonajeMarvel ironMan = new PersonajeMarvel(
                "Tony Stark",
                "Iron Man",
                true,
                "Genio inventor con armadura avanzada",
                "Avengers",
                9.0);
        PersonajeMarvel magneto = new PersonajeMarvel(
                "Erik Lehnsherr",
                "Magneto",
                false,
                "control del magnetismo",
                "X-men",
                9.5);

        PersonajeMarvel capitanAmerica = new PersonajeMarvel(
                "Steve Rogers",
                "Capitán America",
                true,
                "Fuerza sobrehumana, agilidad, y resistencia",
                "Avengers",
                8.8);
        Equipo avengers = new Equipo("Avengers");
        avengers.agregarMiembro(spiderMan);
        avengers.agregarMiembro(ironMan);

        Equipo xmen = new Equipo("X-men");
        xmen.agregarMiembro(magneto);

        System.out.println(avengers.mostrarInformacion());
        System.out.println(xmen.mostrarInformacion());

        Enfrentamiento enfrentamiento = new Enfrentamiento(avengers, xmen);
        System.out.println(enfrentamiento.simularEnfrentamiento());
    }
}