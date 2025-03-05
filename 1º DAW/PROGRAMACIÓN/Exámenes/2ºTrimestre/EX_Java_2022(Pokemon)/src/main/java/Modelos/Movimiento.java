package Modelos;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Movimiento {

    private int id;
    private String nombre;
    private TipoPokemon tipo;
    private TipoAtaque tipoAtaque;
    private Integer potencia;

}
