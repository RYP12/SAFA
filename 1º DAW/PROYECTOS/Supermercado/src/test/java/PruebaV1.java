import org.example.modelos.*;
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

        Cliente Luis = new Cliente(001,
                "12345678A",
                "Luis",
                "Alvarez",
                "Calle Fresa",
                TipoCliente.PARTICULAR);

        System.out.println(Luis);

        Almacen almacen1 = new Almacen(
                0001,
                "Cafeteria",
                700
        );
        System.out.println(almacen1);
    }
}
