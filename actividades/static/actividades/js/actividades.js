var conf1, nombre;
$(document).ready(function(){
    conf1 = {
        title:'Actividad',
        autoOpen: true,
        draggable: true,
        resizable: false,
        position:['center',0], 
        modal:true,
        width: 830,
        show: {
            effect: "drop",
            direction:"up",
            duration: 500
        },
        hide: {
            effect: "drop",
            direction:"up",
            duration: 500
        },
        close: function( event, ui ) {
            $("#formActividad").html("");
        }
    };
    tabla();
    filtros();
    cargarForm();
    cargando();
});

function filtros(){
    $("#Tipo").change(function(){
        window.table.column(1).search($("#Tipo").val()).column(2).search($("#Asignatura").val()).column(3).search($("#Año").val()).column(4).search($("#Periodo").val()).draw();
    });
    $("#Asignatura").change(function(){
        window.table.column(1).search($("#Tipo").val()).column(2).search($("#Asignatura").val()).column(3).search($("#Año").val()).column(4).search($("#Periodo").val()).draw();
    });
    $("#Año").change(function(){
        window.table.column(1).search($("#Tipo").val()).column(2).search($("#Asignatura").val()).column(3).search($("#Año").val()).column(4).search($("#Periodo").val()).draw();
        $("#Año2").removeAttr('disabled');
        if($(this).val() == 0){
            $("#Año2 option[value=0]").prop("selected",true);
            $("#Año2").attr('disabled', 'disabled');;
        }
    });
    $("#Año2").change(function(){
        window.table.column(1).search($("#Tipo").val()).column(2).search($("#Asignatura").val()).column(3).search($("#Año").val()).column(4).search($("#Periodo").val()).column(0).search($(this).val()).draw();
     });
    $("#Periodo").change(function(){
        window.table.column(1).search($("#Tipo").val()).column(2).search($("#Asignatura").val()).column(3).search($("#Año").val()).column(4).search($("#Periodo").val()).draw();
    });
}

function tabla(){
    $.fn.dataTable.TableTools.defaults.aButtons = [ "pdf", "xls" ];
	window.table = $('#actividadT').DataTable({
        "bPaginate": true,
        "bScrollCollapse": true,
        "sPaginationType": "full_numbers",
        "bRetrieve": true,
        "oLanguage": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ Registros",
            "sZeroRecords": "No se encontraron resultados",
            "sInfo": "Mostrando desde _START_ hasta _END_ de _TOTAL_ Registros",
            "sInfoEmpty": "Mostrando desde 0 hasta 0 de 0 Registros",
            "sInfoFiltered": "(filtrado de _MAX_ registros en total)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<<",
                "sPrevious": "<",
                "sNext": ">",
                "sLast": ">>"
            }
        },
        "responsive": true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/actividad/ws/actividades/"

        },
        "drawCallback": function (row, data) {
            editForm();
            singleActividad();
        },
        "columns": [
            {
                "data": "nombre",
                "render": function ( data, type, full, meta ) {
                    if(full.estado === undefined){
                       return "<a class='single btn btn-info' href='/actividad/single/actividad/"+ full.id +"/'>"+ data +"</a> <a class='editar btn btn-info' href='/actividad/edit/actividad/"+ full.id +"/'><i class='icon-pencil'></i></a>";               
                    }else{
                        return "<a class='single btn btn-info' href='/actividad/single/actividad/"+ full.id +"/'>"+ data +"</a>";               
                    }
                }
            },
            {
                "data": "objetivo",
                "orderable":false
            },
            { 
            	"data": "tipo__nombre" 
            },
            {
                "data":"anio",
            },
            {
                "data":"periodo",
                "render": function ( data, type, full, meta ) {
                    if(data==1){
                        return "Primer periodo";
                    }else{
                        return "Segundo periodo";
                    }
                 },
                "orderable":false
            },
            {
                "data": "jefe__nombre", 
                "render": function ( data, type, full, meta ) {
                    nombre = data+" "+full.jefe__apellidos;
                    return nombre;               
                },
                "orderable":false
            }
        ]
    });
    var tt = new $.fn.dataTable.TableTools( window.table,{
        "sRowSelect": 'single',
        "aButtons": [
            {
                "sExtends": "pdf",
                "sButtonText": "Exportar a pdf"
            },
            {
                "sExtends": "xls",
                "sButtonText": "Exportar a excel"

            }
        ]
        
    } );
    $( tt.fnContainer() ).insertAfter('div.info');
    $( tt.fnContainer() ).insertBefore('div.dataTables_wrapper');
}
function singleActividad(){
    $(".single").click(function(){
        $("#formActividad").load($(this).attr('href'),function(){
           $("#myModal").modal('show');    
        });
        return false;
    });
}
function editForm(){
    $(".editar").click(function(){
        $("#formActividad").load($(this).attr('href'),function(){
            validateForm();
            formSteps();
            ajaxFormulario();
            $("#myModal").modal('show');    
        });
        return false;
    });
}
function cargarForm(){
    $("#addActividad").click(function(){
        $("#formActividad").load($(this).attr('href'),function(){
            validateForm();
            formSteps();
            ajaxFormulario();
            $("#myModal").modal('show');    
        });
        return false;
    });
}
function formSteps(){
   var form = $("#form");

    form.steps({
        labels: {
        cancel: "Cancelar",
        current: "current step:",
        pagination: "Paginación",
        finish: "Finalizar",
        next: "Siguiente",
        previous: "Anterior",
        loading: "Cargando ..."
        },
        headerTag: "h4",
        bodyTag: "fieldset",
        transitionEffect: "slideLeft",
        onStepChanging: function (event, currentIndex, newIndex)
        {
            // Allways allow previous action even if the current form is not valid!
            /*if (currentIndex > newIndex)
            {
                return true;
            }
            // Needed in some cases if the user went back (clean up)
            if (currentIndex < newIndex)
            {
                // To remove error styles
                form.find(".body:eq(" + newIndex + ") label.error").remove();
                form.find(".body:eq(" + newIndex + ") .error").removeClass("error");
            }
            form.validate().settings.ignore = ":disabled,:hidden";*/
            return form.valid();
        },
            
        onFinishing: function (event, currentIndex)
        {
            //form.validate().settings.ignore = ":disabled";
            return form.valid();
        },
        onFinished: function (event, currentIndex)
        {
            $("#form").submit();
        }
    });
}
function ajaxFormulario(){
    var options1 = {
        beforeSubmit:function(){
            //cargando();
            return $("#form").valid();
        },
        success: function(response){
            if(response[0].mensaje){
                $("#myModal").modal('hide');    
                window.table.ajax.reload();
            }else{
                for(var i = 0; i<response.length;i++){
                    if(response[i][0]=="username" || response[i][0]=="email"){
                        errorForm(response[i][0],response[i][1]);
                        form.steps("previous");
                    }else if(response[i][0]=="nombre" || response[i][0]=="apellidos" || response[i][0]=="fecha_Nacimiento" || response[i][0]=="sexo" || response[i][0]=="identificacion" || response[i][0]=="telefono" || response[i][0]=="direcion" || response[i][0]=="imagen" || response[i][0]=="hoja_vida"){
                        errorForm(response[i][0],response[i][1]);
                    }
                }
            }
        }
    };
    $('#form').ajaxForm(options1);
}

function errorForm(query,info){
    var consulta1 = "li input[name="+query+"]";
    var consulta2 = "li select[name="+query+"]";
    $(consulta1).parent().find('div').remove();
    $(consulta1).parent().append('<div>'+info+"</div>");
    $(consulta2).parent().find('div').remove();
    $(consulta2).parent().append('<div>'+info+"</div>");
}

function cargando(){

}