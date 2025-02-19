package Modelos;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Item {

    private int id;
    private String nombre;
    private Double aumentoDaño;
    private Double aumentoDefensa;
    private Double aumentoSalud;
    private Double aumentoMana;
}
