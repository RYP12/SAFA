import {useState} from "react";

function FormularioSimple() {

    const [texto, setTexto] = useState("");
    const [mensajeEnviado, setMensajeEnviado] = useState("");

    const manejarCambio = (evento) => {
        setTexto(evento.target.value);
    }

    const manejarEnvio = (evento) => {
        evento.preventDefault();
        setMensajeEnviado(texto);
        setTexto(""); // Para limpiar el input despues de enviarlo
    }

    return (
        <div style={{ border: '1px solid purple', padding: '20px', margin: '20px' }}>
            <h3>Formulario Simple</h3>

            <form onSubmit={manejarEnvio}>
                <label htmlFor="">
                    Escribe tu mensaje:
                    <input type="text"value={texto} onChange={manejarCambio} />
                </label>
                <button type={"submit"}>Enviar</button>
            </form>

            <p>Escribiento: {texto}</p>

            {mensajeEnviado && (
                <p>Enviado: {mensajeEnviado}</p>
            )}
        </div>
    );
}

export default FormularioSimple;