/**
 * Created by mario on 23/04/15.
 */
$(document).ready(function () {
    estadisticas();
    cambio();
    estadisticasFiltroB();
    estadisticasFiltroP();
});
function cambio(){
    $('#Año1_1').change(function(event) {
        $("#Año2_1").removeAttr('disabled');
        if($(this).val()==0){
            $("#Año2_1 option[value=0]").prop("selected",true);
            $("#Año2_1").attr('disabled', 'disabled');
        }
        estadisticasFiltroP();
    });
    $('#Año2_1').change(function(event) {
        estadisticasFiltroP();
    });
    $("#Periodo1").change(function(event) {
        estadisticasFiltroP();
    });
    $('#Año1_2').change(function(event) {
        $("#Año2_2").removeAttr('disabled');
        if($(this).val()==0){
            $("#Año2_2 option[value=0]").prop("selected",true);
            $("#Año2_2").attr('disabled', 'disabled');
        }
        estadisticasFiltroB();
    });
    $('#Año2_2').change(function(event) {
        estadisticasFiltroB();
    });
    $("#Periodo2").change(function(event) {
        estadisticasFiltroB();
    });    
}
function estadisticas() {
    $.ajax({
        url: '/actividad/ws/estadisticas/',
        type: 'POST',
        dataType: 'json',
        success: function (response) {
            columna("#columna",response[0]);
            pie("#pie", response[1]);            
        }
    });
}
function estadisticasFiltroP(){
    $.ajax({
        url: '/actividad/ws/estadistica/p/',
        type: 'POST',
        data:{
            anio1:$('#Año1_1').val(),
            anio2:$('#Año2_1').val(),
            periodo:$('#Periodo1').val()
        },
        dataType: 'json',
        success: function (response) {
            pie("#pieAño", response[0]);
        }
    });
} 
function estadisticasFiltroB(){
    $.ajax({
        url: '/actividad/ws/estadistica/b/',
        type: 'POST',
        data:{
            anio1:$('#Año1_2').val(),
            anio2:$('#Año2_2').val(),
            periodo:$('#Periodo2').val()
        },
        dataType: 'json',
        success: function (response) {
            columna("#columnaAño",response[0]);            

        }
    });
} 
function pie(query,json) {
    $(query).highcharts(json);
}
 
function columna(query,json) {
    $(query).highcharts(json);
}