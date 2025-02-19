package Modelos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;


import java.time.LocalDate;
import java.util.List;


@Data // Creatodos los constructores, getter, setter, hascode, equals y toString necesarios
@AllArgsConstructor
@NoArgsConstructor
public class Personaje {

    private int id;
    private String nombre;
    private String descripcion;
    private LocalDate fechaCreacion;
    private Integer nivel;
    private Double vidaBase;
    private Double manaBase;
    private Double defensaBase;
    private Double defensa;
    private Double ataqueBase;
    private Double ataque;
    private Double vida;
    private Double mana;
    private Region region; // Enumeración de regiones
    private List<Habilidad> habilidades;
    private List<Item> equipamiento;
    private Escalabilidad escalabilidad;


}
