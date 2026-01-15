function ListaAlumnos() {

    const alumnos = ["Ana", "Carlos", "Beatriz", "Daniel"];

    return (
        <div>
            <p>Lista de alumnos:</p>
            <ul>
                {alumnos.map((nombre, indice) =>
                <li key={indice}>{nombre}</li>
                )}
            </ul>

        </div>
    );
}
export default ListaAlumnos;