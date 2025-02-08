package modelos;

import java.util.Objects;

public class Cliente extends Persona {

    private TipoCliente TipoCliente;

    public TipoCliente getTipoCliente() {
        return TipoCliente;
    }

    public void setTipoCliente(TipoCliente tipoCliente) {
        TipoCliente = tipoCliente;
    }

    public Cliente() {
    }

    public Cliente(Integer identificador, String dni, String nombre, String apellido, String direccion, TipoCliente tipoCliente) {
        super(identificador, dni, nombre, apellido, direccion);
        TipoCliente = tipoCliente;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Cliente cliente = (Cliente) o;
        return TipoCliente == cliente.TipoCliente;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), TipoCliente);
    }

    @Override
    public String toString() {
        return "Cliente{" +
                super.toString() +
                ", TipoCliente=" + TipoCliente +
                '}';
    }
}
