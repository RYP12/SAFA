import {useState} from "react";

function GestorNombres() {
    const [listaNombres, setListaNombres] = useState([]);

    const [nuevoNombre, setNuevoNombre] = useState([]);

    const manejarCambio = (evento) => {
        setNuevoNombre(evento.target.value);
    };

    const agregarNombre = (evento) => {
        evento.preventDefault();

        if (nuevoNombre.trim() === "")return;

        setListaNombres([...listaNombres, nuevoNombre]);

        setNuevoNombre("");
    };

    const eliminarNombre = (indiceParaBorrarNombre) => {

        const nuevaListaNombres = listaNombres.filter((_, indiceActual) =>
            indiceActual !==  indiceParaBorrarNombre);
        setListaNombres(nuevaListaNombres);
    };

    return (
      <div>
          <form onSubmit={agregarNombre}>
              <input type="text" value={nuevoNombre} onChange={manejarCambio} placeholder=" Nombre del nombre... " />
              <button type={"submit"}>Añadir</button>
          </form>

          {listaNombres.length === 0 ? (<p>La lista está vacía.</p>) :
              (<ul>
                  {listaNombres.map((nombre, indice) =>
                      <li key={indice}>
                          {nombre}

                          <button type={"button"} onClick={() => eliminarNombre(indice)}> X </button>
                      </li>)}
              </ul>)}
      </div>
    );
}
export default GestorNombres;