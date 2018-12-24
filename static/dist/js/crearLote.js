$(document).ready(function(){
   $("#inpt-proveedor").autocomplete({
    source: function (request, response) {

       var datos = {nombreProveedor: $("#inpt-proveedor").val()};
       console.log(datos);
       var sendData = JSON.stringify(datos);
       $.ajax({
            type: "POST",
            dataType: "json",
            url: "/Proveedor/buscarajax/",
            data: sendData,
            contentType: "application/json; charset=utf-8",
            async: false,
            cache: false,
            CrossDomain: true,

            success: function (jsonfinal) {
            var ListasProveedores = jsonfinal['proveedores'];
            console.log(ListasProveedores);
            response($.map(ListasProveedores, function (item) {
                console.log(item.id);
                return {
                    label: item.nombreProveedor,
                    id: item.id
                    };

            }));

              }
            });
          },
            minLength: 2,
            select: function (event, ui) {
                console.log(ui.item.Id);
                //document.location.href="/Tienda/productoDetalle/"+ui.item.id+"/";
            }

        });

        $( "#search_product" ).autocomplete({
         source: function (request, response) {

            var datos = {nombreProducto: $("#search_product").val()};
            console.log(datos);
            var sendData = JSON.stringify(datos);
            $.ajax({
                 type: "POST",
                 dataType: "json",
                 url: "/Producto/buscarajax/",
                 data: sendData,
                 contentType: "application/json; charset=utf-8",
                 async: false,
                 cache: false,
                 CrossDomain: true,

                 success: function (jsonfinal) {
                 var ListasProductos = jsonfinal['productos'];
                 console.log(ListasProductos);
                 response($.map(ListasProductos, function (item) {
                     console.log(item.id);
                     return {
                         label: item.nombreProducto,
                         id: item.id
                         };

                 }));

                   }
                 });
               },
                 minLength: 2,
                 select: function (event, ui) {
                     $('#cantidad').focus();
                 }

             });

             $('#bt_add').click(function(){
                agregar();
                $('#search_product').focus();
            });
            $('#bt_add').keypress(function(e){
                if(e.which == 13) {
                    $('#search_product').focus();
                }
            });

            ///
            $('#bt_del').click(function(){
                eliminar(id_fila_selected);
            });
            $('#bt_delall').click(function(){
                eliminarTodasFilas();
            });

            $('#bt_GenerarVenta').click(function(){
                GenerarLote();
            });
            $('#inpt-producto').keypress(function(e){
                if(e.keyCode == 13){
                   $('#cantidad').focus();
                }

            });



       });

       function reset_values(){
               //$('#inpt-proveedor').val('');
              // $('#inpt-recibo').val('');
              // $('#inpt-almacen').val('');
               $('#search_product').val('');
               $('#cantidad').val('');

           }
           var cont=0;
           var id_fila_selected=[];
           function agregar(){
               cont++;
               //var combo = document.getElementById("cmbAlmacen");
               //Almacen = combo.options[combo.selectedIndex].text;
               //Almacen = document.getElementById("cmbAlmacen").value;
               Producto = $('#search_product').val();
               cantidad = $('#cantidad').val();
               //imagen = $('#urlImagen').val();
               error = "";
               if (cantidad==''){
                   error = 1;
               }

               if (Producto==''){
                   error = 2;
               }

               if (error=="") {
                   valor = cont - 1;
                   var fila=
                   '<tr class="selected" id="fila'+cont+'" onclick="seleccionar(this.id);"><td>'+cont+'</td>'+

                   '<td>'+Producto+'</td>'+
                   '<td><input type="number" name="cantidad' + valor + '" id="cantidad' + valor + '" required="" class="form-control" value="' + cantidad + '"></td>'+'</tr>';
                   $('#tabla').append(fila);

                   reset_values();
                   reordenar();
               }
               else{
                   switch(error) {
                   case 1:
                       alert("Ingrese una cantidad");
                       $( "#cantidad" ).focus();
                       break;

                   case 2:
                       alert("Ingrese un producto válido");
                       $( "#search_product" ).focus();
                       break;

                   }
               }
           }
           function seleccionar(id_fila){
                   if($('#'+id_fila).hasClass('seleccionada')){
                       $('#'+id_fila).removeClass('seleccionada');
                   }
                   else{
                       $('#'+id_fila).addClass('seleccionada');
                   }
                   //2702id_fila_selected=id_fila;
                   id_fila_selected.push(id_fila);
               }

               function eliminar(id_fila){
                   /*$('#'+id_fila).remove();
                   reordenar();*/

                   for(var i=0; i<id_fila.length; i++){
                       //TotalVenta = TotalVenta - ValorRestar
                       //$('#id_Total').text("S/. "+TotalVenta);
                       $('#'+id_fila[i]).remove();
                   }
                   reordenar();
               }

               function reordenar(){
                   var num=1;
                   $('#tabla tbody tr').each(function(){
                       $(this).find('td').eq(0).text(num);
                       num++;
                   });
               }

               function eliminarTodasFilas(){
               $('#tabla tbody tr').each(function(){
                       $(this).remove();
                   });

               }


               function GenerarLote(){
                   var num=1;
                   oProductoLote = [];
                   contador = 0;
                   $("#tabla tbody tr").each(function (index) {
                       $(this).children("td").each(function (index2) {
                           lotes = [];
                           cont= index -1;
                           console.log(index);
                           switch (index2) {
                               case 1:
                                   Producto = $(this).text();
                                   break;
                               case 2:
                                   cantidad = $("#cantidad"+index ).val();
                                   break;
                           }
                       });
                       contador = 1;
                       oProductoLote.push([cantidad,Producto]);
                   });
                   console.log(oProductoLote);
                   var oProveedor = $('#inpt-proveedor').val();
                   console.log(oProveedor);
                   var comboRecibo = document.getElementById("id_tipoComprobante");
                   var oRecibo = comboRecibo.options[comboRecibo.selectedIndex].text;
                   var oNumRecibo = $('#id_numeroComprobante').val();
                   console.log(oRecibo);
                   //var oPresentacion = document.getElementById("presentacion").value;
                   if (contador == 1) {
                       var datos = {oProductoLote: oProductoLote, oProveedor: oProveedor, oRecibo: oRecibo, oNumRecibo: oNumRecibo, };
                       console.log(datos);
                       var sendData = JSON.stringify(datos);
                       $.ajax({
                           type: "POST",
                           dataType: "json",
                           url: "/Lote/insertar/",
                           data: sendData,
                           contentType: "application/json; charset=utf-8",
                           async: false,
                           cache: false,
                           CrossDomain: true,

                           success: function (result) {
                           //     var id_venta = result["id_venta"];
                                alert('Lote Registrado');
                                document.location.href='/Lote/listar/';

                                //location.reload(true);
                                //document.location.href='/Pedido/listar/';
                           }
                       });
                   }else{
                       alert("No registró ningún lote");
                   }
               }
