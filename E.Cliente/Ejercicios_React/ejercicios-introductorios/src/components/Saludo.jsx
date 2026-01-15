function Saludo ({nombre}){

    return (
        <div style={{ border: '1px solid #ccc', margin: '10px', padding: '10px' }}>
            <p>Bienvenido {nombre}</p>
            <p>Linea de prueba del primer componente de react.</p>
        </div>
    );
}
export default Saludo;