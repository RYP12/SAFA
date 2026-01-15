import {useState} from "react";

function Contador(){

    const [cuenta, setCuenta] = useState(0);

    const incrementar = () => {
        setCuenta(cuenta+1);
    };

    const decrementar = () => {
        setCuenta(cuenta-1);
    }

    const reiniciar = () => {
        setCuenta(0);
    }

    return(
        <div>
            <p >Contador: {cuenta}</p>
            <p style={{color: cuenta < 0 ? "red" : "green"}}>
                {cuenta < 0 ? "Números negativos" : "Números Positivos"}
            </p>
            <button onClick={incrementar}> Sumar </button>
            <button onClick={decrementar}> Restar </button>
            <button onClick={reiniciar}> Reiniciar </button>
        </div>
    );
}

export default Contador;