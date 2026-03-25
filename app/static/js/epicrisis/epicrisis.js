/* Activar/Desactivar Paneles de Busqueda */
const radioButtons = document.querySelectorAll('input[name="toogle"]');
const containerSearchDocumento = document.getElementById("containerSearchDocumento");
const containerSearchHistoria = document.getElementById("containerSearchHistoria");

radioButtons.forEach(radio => {
    radio.addEventListener("change", () => {
        if(radio.id === "searchDocumento"){
            containerSearchDocumento.classList.add("is-active");
            containerSearchDocumento.classList.remove("is-hidden");

            containerSearchHistoria.classList.add("is-hidden");
            containerSearchHistoria.classList.remove("is-active");
        } else if(radio.id === "searchHistoria"){
            containerSearchDocumento.classList.add("is-hidden");
            containerSearchDocumento.classList.remove("is-active");

            containerSearchHistoria.classList.add("is-active");
            containerSearchHistoria.classList.remove("is-hidden");
        }
    })
});

/* Validar Busqueda x Documento */
const busquedaEpicrisisDocumento = document.getElementById("busquedaEpicrisisDocumento");
const validarDocumento = () => {
    let documento = busquedaEpicrisisDocumento.value;
    if(!documento){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar el No. de documento para iniciar la busqueda.",
            icon: "warning"
        })
        .then((result) => {
            if(result.isConfirmed){
                busquedaEpicrisisDocumento.focus();
            };
        });
    } else {
        getRegistrosEpicrisis();
    }
};
busquedaEpicrisisDocumento.addEventListener("keypress", (e) => {
    if(e.key === 'Enter'){
        validarDocumento();
    };
});

/* API Fetch Busqueda Epicrisis por Medico y Paciente */
const medico = document.getElementById("medico");
const tablaEpicrisis = document.getElementById("tablaEpicrisis");
const getRegistrosEpicrisis = () => {
    let med = medico.value;
    let paciente = busquedaEpicrisisDocumento.value;
    /* Limpiar Tabla */
    while(tablaEpicrisis.rows.length > 1){
        tablaEpicrisis.deleteRow(1);
    };
    /* Fetch */
    fetch("/getRegistrosEpicrisis", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ med, paciente })
    })
    .then(response => response.json())
    .then(data => {
        /* Validar si hay resultados */
        if(!Array.isArray(data) || data.length === 0){
            Swal.fire({
                title: "Advertencia!",
                text: "No se encontraron registros asociados.",
                icon: "warning"
            });
            return;
        };

        /* Resultados */
        data.forEach(registro => {
            tablaEpicrisis.insertRow().innerHTML = `
                <td scope="col" style="width: 5%; font-size: small;">${registro.id}</td>
                <td scope="col" style="width: 15%; font-size: small;">${registro.ingreso}</td>
                <td scope="col" style="width: 15%; font-size: small;">${registro.hora}</td>
                <td scope="col" style="width: 15%; font-size: small;">${registro.codigo}</td>
                <td scope="col" style="width: 30%; font-size: small;">${registro.nombre}</td>
                <td scope="col" style="width: 10%; font-size: small;"></td>
                <td scope="col" style="width: 10%; font-size: small;">
                
                </td>
            `
        });

    })
    .catch(error => console.error("error: ", error))
}