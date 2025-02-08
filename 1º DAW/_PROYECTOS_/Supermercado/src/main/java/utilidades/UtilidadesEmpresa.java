package utilidades;

import modelos.Empleado;
import modelos.Empresa;
import modelos.TipoContrato;
import modelos.TipoEmpresa;

import java.util.*;

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

    //MAPAS

    public Map<TipoEmpresa, Integer> getNumEmpresasPorTipo(List<Empresa> empresas){
        Map<TipoEmpresa, Integer> numEmpresasPorTipo= new HashMap<>();
        for (Empresa empresa : empresas){
            if (!numEmpresasPorTipo.containsKey(empresa.getTipoEmpresa())){
                numEmpresasPorTipo.put(empresa.getTipoEmpresa(), 1);
            } else {
                numEmpresasPorTipo.put(empresa.getTipoEmpresa(), numEmpresasPorTipo.get(empresa.getTipoEmpresa()) + 1);
            }
        }
        return numEmpresasPorTipo;
    }

    public Map<TipoEmpresa,Integer> getNumEmpleadosPorTipoEmpresa(List<Empresa> empresa){
        Map<TipoEmpresa, Integer> numEmpleadosPorTipo= new HashMap<>();
        for (Empresa emp : empresa){
            if (!numEmpleadosPorTipo.containsKey(emp.getTipoEmpresa())){
                numEmpleadosPorTipo.put(emp.getTipoEmpresa(), emp.getEmpleados().size());
            } else {
                numEmpleadosPorTipo.put(emp.getTipoEmpresa(), numEmpleadosPorTipo.get(emp.getTipoEmpresa()) + emp.getEmpleados().size());
            }
        }
        return numEmpleadosPorTipo;
    }

    public Map<TipoContrato, List<Empleado>> getEmpleadosPorTipoContrato(Empresa empresas){
        Map<TipoContrato, List<Empleado>> empleadosPorTipoContrato= new HashMap<>();
        for (Empleado empleado : empresas.getEmpleados()){
            if (!empleadosPorTipoContrato.containsKey(empleado.getContrato().getTipoContrato())){
                empleadosPorTipoContrato.put(empleado.getContrato().getTipoContrato(), new ArrayList<>(List.of(empleado)));
            } else {
                empleadosPorTipoContrato.get(empleado.getContrato().getTipoContrato()).add(empleado);
            }
        }
        return empleadosPorTipoContrato;
    }

    public Map<Empresa, Map<TipoContrato, List<Empleado>>> getEmpleadosPorTipoContrato(List<Empresa> empresas){
        Map<Empresa, Map<TipoContrato, List<Empleado>>> empleadosPorTipoContrato= new HashMap<>();
        for (Empresa empresa : empresas){
            empleadosPorTipoContrato.put(empresa, getEmpleadosPorTipoContrato(empresa));
        }
        return empleadosPorTipoContrato;
    }

    public List<Empleado> getEmpleadosPymePracticas(List<Empresa> empresas){
        List<Empleado> empleadosPymePracticas= new ArrayList<>();
        for (Empresa empresa : empresas){
            if (empresa.getTipoEmpresa().equals(TipoEmpresa.PYME)){
                for (Empleado empleado : empresa.getEmpleados()){
                    if (empleado.getContrato().getTipoContrato().equals(TipoContrato.PRACTICAS)){
                        empleadosPymePracticas.add(empleado);
                    }
                }
            }

        }
        return empleadosPymePracticas;
    }

    public Map<Empresa,Empleado> getLosMejorPagadosPorEmpresa(List<Empresa> empresas){
        Map<Empresa,Empleado> losMejorPagados= new HashMap<>();
        for (Empresa empresa : empresas){
            losMejorPagados.put(empresa, getMileuristasOrdenadosPorSalario(empresa).getFirst());
        }

        return losMejorPagados;
    }




}
