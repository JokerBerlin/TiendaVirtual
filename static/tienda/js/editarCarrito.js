function editarCarrito(idCarro){
    cantidad = $('#cambiarValor'+idCarro+'').val();
    //alert(idProducto+'hola'+cantidad);
    var datos = {idCarro: idCarro, cantidad: cantidad, };
    console.log(datos);
    var sendData = JSON.stringify(datos);
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/Carro/editar/",
        data: sendData,
        contentType: "application/json; charset=utf-8",
        async: false,
        cache: false,
        CrossDomain: true,

        success: function (result) {
        //     var id_venta = result["id_venta"];
             //alert('Carro registrado');

             location.reload(true);
             //document.location.href='/Pedido/listar/';
        }
    });
}
