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
        getRegistrosEpicrisisDoc();
    }
};
busquedaEpicrisisDocumento.addEventListener("keypress", (e) => {
    if(e.key === 'Enter'){
        validarDocumento();
    };
});

const medico = document.getElementById("medico");
const tablaEpicrisis = document.getElementById("tablaEpicrisis");

/* API Fetch Busqueda Epicrisis por Medico y Paciente */
const getRegistrosEpicrisisDoc = () => {
    let med = medico.value;
    let paciente = busquedaEpicrisisDocumento.value;
    /* Limpiar Tabla */
    while(tablaEpicrisis.rows.length > 1){
        tablaEpicrisis.deleteRow(1);
    };
    /* Fetch */
    fetch("/getRegistrosEpicrisisDoc", {
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
                <td style="width: 5%; font-size: small;">${registro.id}</td>
                <td style="width: 15%; font-size: small;">${registro.ingreso}</td>
                <td style="width: 15%; font-size: small;">${registro.hora}</td>
                <td style="width: 15%; font-size: small;">${registro.codigo}</td>
                <td style="width: 30%; font-size: small;">${registro.nombre}</td>
                <td style="width: 10%; font-size: small;">${registro.historia}</td>
                <td style="width: 10%; font-size: small;">
                    <a onclick="activarModal()" class="button is-small is-info has-tooltip-bottom" data-tooltip="Vista Previa">
                        <span class="icon is-small"><i aria-hidden="true"><img src="./static/img/icons/pdf.png" alt="icon"></i></span>
                    </a>
                </td>
            `
        });

    })
    .catch(error => console.error("error: ", error))
}

/* Validar Busqueda por Atención */
const busquedaEpicrisisHistoria = document.getElementById("busquedaEpicrisisHistoria");
const validarHistoria = () => {
    let historia = busquedaEpicrisisHistoria.value;
    if(!historia){
        Swal.fire({
            title: "Advertencia!",
            text: "Debe diligenciar el No. de historia para iniciar la busqueda.",
            icon: "warning"
        })
        .then((result) => {
            if(result.isConfirmed){
                busquedaEpicrisisHistoria.focus();
            }
        });
    } else {
        alert("Prueba Exitosa");
    };
};
busquedaEpicrisisHistoria.addEventListener("keypress", (e) => {
    if(e.key === 'Enter'){
        validarHistoria();
    };
});

/* API Fetch Busqueda Epicrisis x Medico y Atención */
const getRegistrosEpicrisisHisto = () => {
    let med = medico.value;
    let historia = busquedaEpicrisisHistoria.value;
    /* Limpiar tabla */
    while(tablaEpicrisis.rows.length > 1){
        tablaEpicrisis.deleteRow(1);
    };
    /* Fetch */
    fetch("/getRegistrosEpicrisisHisto", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ med, historia })
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
                <td style="width: 5%; font-size: small;">${registro.id}</td>
                <td style="width: 15%; font-size: small;">${registro.ingreso}</td>
                <td style="width: 15%; font-size: small;">${registro.hora}</td>
                <td style="width: 15%; font-size: small;">${registro.codigo}</td>
                <td style="width: 30%; font-size: small;">${registro.nombre}</td>
                <td style="width: 10%; font-size: small;">${registro.historia}</td>
                <td style="width: 10%; font-size: small;">
                
                </td>
            `
        });
    })
    .catch(error => console.error("error: ", error))
};

/* Activar/Desactivar Modal Vista Previa */
const modalVistaPrevia = document.getElementById("modalVistaPrevia");
const activarModal = () => {
    modalVistaPrevia.classList.remove("is-hidden");
    modalVistaPrevia.classList.add("is-active");
}