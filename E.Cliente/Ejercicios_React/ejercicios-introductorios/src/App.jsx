import Saludo from "./components/Saludo.jsx";
import Contador from "./components/Contador.jsx";
import ListaAlumnos from "./components/ListaAlumnos.jsx";
import FormularioSimple from "./components/FormularioSimple.jsx";
import GestorNombres from "./components/GestorNombres.jsx";
import FormularioValidado from "./components/FormularioValidado.jsx";

function App() {
    return (
        <div>
            <h2>Ejercicio Saludo:</h2>
            <Saludo nombre={"Juan"} />
            <Saludo nombre={"Pepe"} />

            <h2>Ejercicio Contador:</h2>
            <Contador />

            <h2>Ejercicio ListaAlumnos:</h2>
            <ListaAlumnos />

            <h2>Ejercicio FormularioSimple:</h2>
            <FormularioSimple />

            <h2>Gestor de nombres:</h2>
            <GestorNombres/>

            <h2>Formulario Validado: </h2>
            <FormularioValidado />
        </div>
    );
}

export default App;