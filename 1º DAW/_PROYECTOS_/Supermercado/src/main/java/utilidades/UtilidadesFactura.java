package utilidades;

import modelos.Cliente;
import modelos.Factura;
import modelos.LineaFactura;

import java.time.LocalDate;
import java.util.List;

public class UtilidadesFactura {

    // Comparar fechas de vencimiento
   public boolean esFacturaVencida(Factura factura) {

       if (factura.getFechaVencimiento().isEqual(LocalDate.now()) || factura.getFechaVencimiento().isBefore(LocalDate.now())) {
           return true;
       } else {
           return false;
       }
   }

   // Calcular importe base de la factura

    public Double calcularBaseFactura (Factura factura) {

       Double baseImporte = 0.00;
       
       for (LineaFactura producto : factura.getLineasFactura()) {

           Double importeProducto = producto.getProducto().getPrecio();

           Integer cantidad = producto.getCantidad();

           baseImporte += importeProducto * cantidad;

       }
       return baseImporte;
    }

    // Calcular total a pagar

    public Double calcularTotalAPagar (Factura factura) {

       Double impBase = factura.getImporteBase();

       Double descuentos = factura.getDescuento();

       Double iva = factura.getIva();

       return (impBase + descuentos) * iva;

    }

    public Double gastoTotalCliente(List<Factura> facturas, Cliente cliente) {
        Double totalCliente = 0.0;
        for (Factura factura : facturas) {
            if (factura.getCliente().equals(cliente)) {
                totalCliente += factura.getImporteBase();
            }
        }
        return totalCliente;
    }

    public Double totalFacturadoPeriodo(List<Factura> facturas, LocalDate fechaInicio, LocalDate fechaFin) {
        Double totalFacturado = 0.0;
        for (Factura factura : facturas) {
            if (fechaInicio.isAfter(factura.getFechaEmision()) && fechaFin.isBefore(factura.getFechaEmision())) {
                totalFacturado += factura.getImporteBase();
            }
        }
        return totalFacturado;
    }








}












