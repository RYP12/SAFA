package modelos;

import java.time.LocalDate;
import java.util.List;
import java.util.Objects;

public class Factura {
    private int identificador;
    private String codigoFactura;
    private double importeBase;
    private double descuento;
    private double iva;
    private double totalAPagar;
    private LocalDate fechaEmision;
    private LocalDate fechaVencimiento;
    private boolean pagada;
    private List<LineaFactura> lineasFactura;
    private Cliente cliente;

    // Constructores
    public Factura(int identificador, String codigoFactura, double importeBase, double descuento, double iva, double totalAPagar, LocalDate fechaEmision, LocalDate fechaVencimiento, boolean pagada, List<LineaFactura> lineasFactura, Cliente cliente) {
        this.identificador = identificador;
        this.codigoFactura = codigoFactura;
        this.importeBase = importeBase;
        this.descuento = descuento;
        this.iva = iva;
        this.totalAPagar = totalAPagar;
        this.fechaEmision = fechaEmision;
        this.fechaVencimiento = fechaVencimiento;
        this.pagada = pagada;
        this.lineasFactura = lineasFactura;
        this.cliente = cliente;
    }

    public Factura() {
    }

    // Getter y Setter


    public int getIdentificador() {
        return identificador;
    }

    public void setIdentificador(int identificador) {
        this.identificador = identificador;
    }

    public String getCodigoFactura() {
        return codigoFactura;
    }

    public void setCodigoFactura(String codigoFactura) {
        this.codigoFactura = codigoFactura;
    }

    public double getImporteBase() {
        return importeBase;
    }

    public void setImporteBase(double importeBase) {
        this.importeBase = importeBase;
    }

    public double getDescuento() {
        return descuento;
    }

    public void setDescuento(double descuento) {
        this.descuento = descuento;
    }

    public double getIva() {
        return iva;
    }

    public void setIva(double iva) {
        this.iva = iva;
    }

    public double getTotalAPagar() {
        return totalAPagar;
    }

    public void setTotalAPagar(double totalAPagar) {
        this.totalAPagar = totalAPagar;
    }

    public LocalDate getFechaEmision() {
        return fechaEmision;
    }

    public void setFechaEmision(LocalDate fechaEmision) {
        this.fechaEmision = fechaEmision;
    }

    public LocalDate getFechaVencimiento() {
        return fechaVencimiento;
    }

    public void setFechaVencimiento(LocalDate fechaVencimiento) {
        this.fechaVencimiento = fechaVencimiento;
    }

    public boolean isPagada() {
        return pagada;
    }

    public void setPagada(boolean pagada) {
        this.pagada = pagada;
    }

    public List<LineaFactura> getLineasFactura() {
        return lineasFactura;
    }

    public void setLineasFactura(List<LineaFactura> lineasFactura) {
        this.lineasFactura = lineasFactura;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }


    // Equals y Hashcode

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Factura factura = (Factura) o;
        return identificador == factura.identificador && Double.compare(importeBase, factura.importeBase) == 0 && Double.compare(descuento, factura.descuento) == 0 && Double.compare(iva, factura.iva) == 0 && Double.compare(totalAPagar, factura.totalAPagar) == 0 && pagada == factura.pagada && Objects.equals(codigoFactura, factura.codigoFactura) && Objects.equals(fechaEmision, factura.fechaEmision) && Objects.equals(fechaVencimiento, factura.fechaVencimiento) && Objects.equals(lineasFactura, factura.lineasFactura) && Objects.equals(cliente, factura.cliente);
    }

    @Override
    public int hashCode() {
        return Objects.hash(identificador, codigoFactura, importeBase, descuento, iva, totalAPagar, fechaEmision, fechaVencimiento, pagada, lineasFactura, cliente);
    }

    // tostring


    @Override
    public String toString() {
        return "Factura{" +
                "identificador=" + identificador +
                ", codigoFactura='" + codigoFactura + '\'' +
                ", importeBase=" + importeBase +
                ", descuento=" + descuento +
                ", iva=" + iva +
                ", totalAPagar=" + totalAPagar +
                ", fechaEmision=" + fechaEmision +
                ", fechaVencimiento=" + fechaVencimiento +
                ", pagada=" + pagada +
                ", lineasFactura=" + lineasFactura +
                ", cliente=" + cliente +
                '}';
    }
}
