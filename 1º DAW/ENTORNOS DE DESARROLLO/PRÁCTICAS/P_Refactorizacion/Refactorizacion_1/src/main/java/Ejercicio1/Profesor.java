package Ejercicio1;

import java.util.List;

public class Profesor extends Persona {

    // variable llamada str cuando deberia llamarse nombre
    String nombre;
    int edad;
    // varible numeroDeTelefono eliminada por estar duplicada
    List<Prestamo> prestamos;

    public Profesor(String numeroDeTelefono) {
        super(numeroDeTelefono);

        System.out.println("Nombre: " + nombre);

        System.out.println("Edad: " + edad);

        System.out.println("Numero de telefono: " + numeroDeTelefono);
    }

    public void printTodaLaInformacion() {

        // Metodo que ha sido extraido con refactor extract para no repetir codigo en cada funcion
        informacionTotal();

        for (Prestamo p: prestamos){
            System.out.println("PRESTAMOS: " + p);
        }
    }

    private void informacionTotal() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Telefono: " + nuemeroDeTelefono);
    }
}
