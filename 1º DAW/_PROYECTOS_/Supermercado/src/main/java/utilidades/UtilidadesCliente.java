package utilidades;

import modelos.Cliente;

public class UtilidadesCliente {

    public Boolean esDniValido(Cliente cliente) {

        String datosDNI = cliente.getDni();

        if (datosDNI.length() == 9) {

            Integer contador = 1;

            for(char letra : cliente.getDni().toCharArray()) {

                if (!Character.isDigit(letra) && contador <= 0) {
                    return false;
                }

                if (Character.isDigit(letra) && contador < 0) {
                    return false;
                }

                contador++;
            }
            return true;

        }else{
            return false;
        }

    }

}
