package org.example.utilidades;

import org.example.modelos.Factura;
import org.example.modelos.LineaFactura;
import org.example.modelos.Producto;

import java.time.LocalDate;

public class UtilidadesFactura {

    public boolean esFacturaVencida(Factura factura) {
        if (factura == null || factura.getFechaVencimiento() == null) {
            return false;
        }
        return factura.getFechaVencimiento().isBefore(LocalDate.now());
    }

    public boolean calcularBaseFactura(Factura factura) {

        double precioBase;

        for (LineaFactura){

            precioBase = Producto.precio() += Producto.precio();


        }
    }

}
