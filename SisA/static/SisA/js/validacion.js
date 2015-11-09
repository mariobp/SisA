/**
 * Created by mario on 15/12/13.
 */
$(document).on('ready', function () {
    validateForm();
});

function validateForm(){
    $.validator.addMethod("DateFormat", function (value, element) {
            return value.match(/^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$/);
        },
        "Digite una fecha en el formato dd/mm/yy"
    );
    $.validator.addMethod('Imgfilesize', function (value, element, param) {
            // param = size (en bytes)
            // element = element to validate (<input>)
            // value = value of the element (file name)
            return this.optional(element) || (element.files[0].size <= param);
        },
        "File must be JPG, GIF or PNG, less than 1MB"
    );
    $.validator.addMethod("maxfilesize", function (value, element) {
            return this.optional(element) || (element.files && element.files[0] && element.files[0].size < 1024 * 500 && element.files[0].size != 0);
        },
        'El archivo no puede tener un tamaño de 0 bytes o                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               exceder los 5MB.'
    );
    $('#form').validate({
        rules: {
            nombre: {
                required: true,
                minlength: 2
            },
            apellidos: {
                required: true,
                minlength: 2
            },
            fecha_Nacimiento: {
                required: true,
                DateFormat: true
            },
            sexo: {
                required: true
            },
            telefono: {
                required: true,
                number: true,
                minlength: 6,
                maxlength: 10

            },
            identificacion: {
                required: true,
                number: true,
                minlength: 8,
                maxlength: 15

            },
            direcion: {
                required: true
            },
            codigo: {
                required: true,
                number: true,
                minlength: 2
            },
            semestre:{
                required: true
            },
            programa:{
                required: true
            },
            email: {
                required: true,
                email: true,
                remote:{
                    url:'/actividad/ws/validar/mail/',
                    type:'POST',
                    data:{
                        email:function(){
                            return $("#id_email").val();
                        }
                    }
                }
            },
            anio: {
                required: true
            },
            username: {
                required: true,
                remote:{
                    url:'/actividad/ws/validar/user/',
                    type:'POST',
                    data:{
                        username: function(){
                            return $("#id_username").val();
                        }
                    }
                }
            },
            password: {
                required: true
            },
            newPassword1: {
                required: true,
                minlength: 6
            },
            newPassword2: {
                required: true,
                minlength: 6
            },
            password_one:{
                required: true,
                minlength:2
            },
            password_two:{
                required:true,
                minlength:2,
                equalTo:"#id_password_one"
            },
            subtema: {
                required: true
            },
            imagen: {
                maxfilesize: true,
                extension: "png|jpe?g"
                },
        },
        messages:{
            username:{
                remote:'Ya existe un usuario con ese nombre'
            },
            email:{
                remote:'Ya existe un usuario con ese email</div></div>'
            }
        }
        ,
        highlight: function (element) {
            $(element).closest('.label').removeClass('success').addClass('error');
            $(element).closest('.input').removeClass('success').addClass('error');
        },
        success: function (element) {
            element
                .html('Ok').addClass('valid')
                .closest('.label').removeClass('error').addClass('success')
                .closest('.input').removeClass('error').addClass('success');
        }
    });
}