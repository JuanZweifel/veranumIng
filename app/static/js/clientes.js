let dataTable;
let dataTableIsInitialized;



const dataTableOptions = {
    columnDefs: [
        {className: "centered", targets: [0,1,2,3,4,5,6,7] },
        {orderable:false, targets:[1,3,5,6]},
        {searchable:false,targets:[1,7]},

    ],
    pageLength: 4,
    destroy: true
};


const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listaclientes();

    dataTable = $("#datatable-responsive").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};



const listaclientes=async()=>{
    try {
        const response =await fetch("http://127.0.0.1:8000/lista_clientes/")
        const data=await response.json();

        let content = ``;
        data.clientes.forEach((cliente) => {
            content += `
                <tr>
                    <td>${cliente.run}</td>
                    <td>${cliente.dv}</td>
                    <td>${cliente.primer_nombre}</td>
                    <td>${cliente.segundo_nombre}</td>
                    <td>${cliente.apellido_paterno}</td>
                    <td>${cliente.apellido_materno}</td>
                    <td>${cliente.correo}</td>
                    <td>
                    <a href="modificar_perfil/ ${cliente.run}" role="button" class="btn btn-primary text-light">Modificar</a>
                    <a href="#" role="button" class="btn btn-danger text-light">Eliminar</a> </td>
                    </td>
                </tr>`;
        });
        table_body_clientes.innerHTML = content;
        
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener('load', async()=>{
    await initDataTable();
});


