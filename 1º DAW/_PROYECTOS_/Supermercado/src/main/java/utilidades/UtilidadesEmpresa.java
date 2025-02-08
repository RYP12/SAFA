package utilidades;

import modelos.Empleado;
import modelos.Empresa;
import modelos.TipoContrato;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class UtilidadesEmpresa {

    //Obtener lista de empleados que coincidan con el tipo de contrato especificado
    public List<Empleado> getEmpleadosPorContrato(Empresa empresa, TipoContrato tipoContrato) {
        List <Empleado> empleados = new ArrayList<Empleado>();
        for (Empleado empleado : empresa.getEmpleados()) {
            if (empleado.getContrato().getTipoContrato().equals(tipoContrato)) {
                empleados.add(empleado);
            }
        }
        return empleados;

    }

    //Lista de empleados cuyo salario es mayor o igual a 1000€

    public List<Empleado> getMileuristasOrdenadosPorSalario(Empresa empresa){
        List <Empleado> empleados = new ArrayList<Empleado>();
        for (Empleado empleado : empresa.getEmpleados()){
            if (empleado.getContrato().getSalarioBase() >= 1000){
                empleados.add(empleado);
            }
        }
        empleados.sort(Comparator.comparing(c-> c.getContrato().getSalarioBase()));
        empleados.reversed();
        return empleados;
    }

    //Fondo Salarial de la empresa: Remite el salario de todos los empleados de la empresa

    public Double fondoSalarialEmpresa(Empresa empresa){
        Double sumaPrecio = 0.0;
        for (Empleado empleado : empresa.getEmpleados()){

            Double salario = empleado.getContrato().getSalarioBase();
            sumaPrecio += salario;

        }
        return sumaPrecio;
    }

    //Empleado mejor pagado

    public Empleado getMejorPagado(List<Empresa> empresas){
        List <Empleado> empleados = new ArrayList<Empleado>();
        for (Empresa empresa : empresas){
            for (Empleado empleado : empresa.getEmpleados()){
                empleados.add(empleado);
            }
        }
        empleados.sort(Comparator.comparing(c-> c.getContrato().getSalarioBase()));
        empleados.reversed();
        return empleados.get(0);
    }



}
