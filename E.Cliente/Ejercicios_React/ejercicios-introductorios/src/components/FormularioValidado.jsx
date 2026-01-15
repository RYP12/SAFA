import {useState} from "react";

function FormularioValidado(){

    const [nombre, setNombre] = useState("");
    const [email, setEmail] = useState("");

    const [error, setError] = useState("");

    const manejarEnvio = (evento) => {
        evento.preventDefault();

        if (nombre === "" || email === "") {
            setError("!!Por favor rellenes todos los campos requeridos!!");
            return;
        }

        if (!email.includes("@")) {
            setError("El email no es válido");
        }

        setNombre("");
        setEmail("");
    }
    return (
      <div>
          <form onSubmit={manejarEnvio}>
              <div>
                  <label>Nombre: </label>
                  <input type="text" value={nombre}
                         onChange={(evento) => setNombre(evento.target.value)} />
              </div>

              <div>
                  <label>Email: </label>
                  <input type="text" value={email}
                         onChange={(evento) => setEmail(evento.target.value)} />
              </div>

              {error !==  "" ? (
                  <p style={{color:"red",fontWeight:"bold"}}>
                      ERROR: {error}
                  </p>
              ) : (
                  <p style={{color:"green",fontWeight:"bold"}} >TODO  CORRECTO</p>
              )}

              <button type="submit">Enviar</button>
          </form>
      </div>
    );
};
export default FormularioValidado;