import org.example.modelos.Almacen;
import org.example.modelos.Cliente;
import org.example.modelos.Producto;
import org.example.modelos.TipoProducto;
import org.w3c.dom.ls.LSOutput;

import java.time.LocalDate;

public class PruebaV1 {
    public static void main(String[] args) {
        Producto Cafe = new Producto(
                01,
                "001",
                "Cafe Irlandes",
                LocalDate.of(2025, 12, 10),
                TipoProducto.ALIMENTO);

        System.out.println(Cafe);

        Cliente Luis = new Cliente(

        );
        Almacen almacen1 = new Almacen();
    }
}
