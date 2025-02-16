public class PersonajeMarvel implements Poderes, Mostrable {

    private String nombre;
    private String alias;
    private boolean esHeroe;
    private String poderPrincipal;
    private String afiliacion;
    private double poder;

    public PersonajeMarvel(String nombre, String alias, boolean esHeroe, String poderPrincipal, String afiliacion, double poder) {
        this.nombre = nombre;
        this.alias = alias;
        this.esHeroe = esHeroe;
        this.poderPrincipal = poderPrincipal;
        this.afiliacion = afiliacion;
        this.poder = poder;
    }




    @Override
    public double obtenerPoder() {
        return poder;
    }


    @Override
    public String mostrarInformacion() {
        String tipo = esHeroe ? "Es Heroe" : "No es un heroe";
        return nombre + " (" + alias + "). Su poder principal es " + poderPrincipal + ".\n" +
                "Su afiliacion, " + afiliacion + ". " + tipo + ". Su poder es de " + poder + ".";
    }
}