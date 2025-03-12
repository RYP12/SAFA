package Ejercicio1;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data


public class Persona {

    String nuemeroDeTelefono;

    public Persona(String nuemeroDeTelefono) {
        super();
        this.nuemeroDeTelefono = nuemeroDeTelefono;
    }

    public String getNuemeroDeTelefono() {
        return nuemeroDeTelefono;
    }

    public void setNuemeroDeTelefono(String nuemeroDeTelefono) {
        this.nuemeroDeTelefono = nuemeroDeTelefono;
    }




}

