$(document).ready(function(){
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
              console.log(ui.item.Id);
              document.location.href="/Tienda/productoDetalle/"+ui.item.id+"/";
          }

      });

       });
