package utilidades;

import modelos.Almacen;
import modelos.Producto;
import modelos.TipoProducto;

import java.util.ArrayList;
import java.util.List;

public class UtilidadesProductos {

    List<Producto> productos;

    public List <Producto> getPorTipo(List<Producto> productos, TipoProducto tipo) {

        for (Producto producto : productos) {
            if (producto.getTipoProducto() == tipo) {
                this.productos.add(producto);
            }
        }
        return productos;

    }

    public List<Producto> getPorAlmacen(List<Producto> productos, Almacen almacen) {

        for (Producto producto : productos) {

            if (producto.getAlmacen() == almacen){
                this.productos.add(producto);
            }
        }
        return productos;

    }

}
