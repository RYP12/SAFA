package Modelos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor

public class Habilidad {
    private int id;
    private String nombre;
    private Double dañoBase;
    private Double daño;
    private Double costeMana;
    private TipoHabilidad tipoHabilidad;


}
