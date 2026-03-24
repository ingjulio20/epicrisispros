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