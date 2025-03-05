package Modelos;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor

public class Entrenador {

    private int id;
    private String nombre;
    private String apellidos;
    private LocalDate fechaNacimiento;
    private List<TipoPokemon> tiposPreferidos;
    private List<Pokemon> equipoPokemon;


}
