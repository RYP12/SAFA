package utilidades;

import modelos.Factura;

import java.time.LocalDate;

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

    public double calcularBaseFactura(Factura factura) {

       
       for (double baseFactura = 0; factura.getLineasFactura().size() != 0; baseFactura++) {

           System.out.println(baseFactura);

       }
    }
}












