let tableModalPacientes = new DataTable('#tablaModalPacientes', {
    language: {
        "lengthMenu": "_MENU_ registros",
        "search": "Filtrar:",
        "zeroRecords": "No se encontrarón registros",
        "emptyTable":  "No existen registros disponibles",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "paginate": {
            "first": "Primera",
            "last": "Ultima",
            "next": "Siguiente",
            "previous": "Prevío"
        },
    }
});

let tableModalEvoluciones = new DataTable('#tablaModalEvoluciones', {
    language: {
        "lengthMenu": "_MENU_ registros",
        "search": "Filtrar:",
        "zeroRecords": "No se encontrarón registros",
        "emptyTable":  "No existen registros disponibles",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "paginate": {
            "first": "Primera",
            "last": "Ultima",
            "next": "Siguiente",
            "previous": "Prevío"
        },
    }
});

let tableModalDiagnosticos = new DataTable('#tablaModalDiagnosticos', {
    language: {
        "lengthMenu": "_MENU_ registros",
        "search": "Filtrar:",
        "zeroRecords": "No se encontrarón registros",
        "emptyTable":  "No existen registros disponibles",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "paginate": {
            "first": "Primera",
            "last": "Ultima",
            "next": "Siguiente",
            "previous": "Prevío"
        },
    }
});

let tableEpicrisis = new DataTable('#tablaEpicrisis', {
    language: {
        "lengthMenu": "_MENU_ registros",
        "search": "Filtrar:",
        "zeroRecords": "No se encontrarón registros",
        "emptyTable":  "No existen registros disponibles",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "paginate": {
            "first": "Primera",
            "last": "Ultima",
            "next": "Siguiente",
            "previous": "Prevío"
        }
    },
    columnDefs: [{ orderable: false, targets: 1 }],
    order: [[0, 'desc']]
});

let tablePrevaloraciones = new DataTable('#tablaPrevaloraciones', {
    language: {
        "lengthMenu": "_MENU_ registros",
        "search": "Filtrar:",
        "zeroRecords": "No se encontrarón registros",
        "emptyTable":  "No existen registros disponibles",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
        "paginate": {
            "first": "Primera",
            "last": "Ultima",
            "next": "Siguiente",
            "previous": "Prevío"
        },
    }
});