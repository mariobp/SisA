var conf;
var pleaseWaitDiv = $('<div class="modal hide" id="pleaseWaitDialog" data-backdrop="static" data-keyboard="false"><div class="modal-header"><h1>Processing...</h1></div><div class="modal-body"><div class="progress progress-striped active"><div class="bar" style="width: 100%;"></div></div></div></div>');
$(document).ready(function(){
    formSteps();
    fecha();
    ajaxFormulario();
    conf = {
        title:'Guardado',
        autoOpen: true,
        draggable: false,
        resizable: false,
		my: "top",
        at: "center top", 
        modal:true,
        width: 640,
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
        buttons:[
            {
                id:"cerrar",
                text:"Cerrar",
                click: function(){
                    $(this).dialog('close');
                    form.steps("previous");
                }
            },
            {
            	id:"login",
            	text:"Iniciar Sesión",
            	click: function(){
            		 window.location = '/login/'
            	}	
            }
        ]
    };
    cargando();
});

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
        	cargando();
            return $("#form").valid();
        },
        success: function(response){
			pleaseWaitDiv.modal('hide');
            if(response[0].mensaje){
            	document.getElementById("form").reset();
            	$("#dialog").append('<p>Registrado Correctamente.</p>').dialog(conf);
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
	var myApp;
	myApp = myApp || (function () {
    return {
        showPleaseWait: function() {
            pleaseWaitDiv.modal();
        }
    };
	})();
}