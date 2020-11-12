
 
$(function()
	{
    
    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
				'ÁÉÍÓÚáéíóú- ';
	
    
	
                
    $('txtRutt, .txtNombr, .txtApellido, .txtCorreo, .txtPass, .Telefono, .nacimiento, .selectCiudad, .selectReg, .selectEd').keypress(function(e)
    {
        let caracter= String.fromCharCode(e.wich);
        if(numeros.indexOf(caracter)<0)
            return false;

    });

    $('.btnEnviar').click(function()
    {
        
		
		if($('.txtRutt').val() == '')
		{
            
			alert('No especificó el rut');
			$('.txtRutt').focus();
            return;
            			
		}
		
		
		if($('.txtNomb').val() == '')
		{
			alert('No especificó el nombre');
			$('.txtNomb').focus();
			return;			
		}

		if($('.txtApellid').val() == '')
		{
			alert('No especificó el apellido');
			$('.txtApellid').focus();
			return;			
		}
        		
        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/
        texto= $('.txtCorre').val();

        if(!emailRegex.test($('.txtCorre').val()))
        {
            alert('Verificar formato correo');
            $('.txtCorre').focus();
            return;
        }
        if($('.txtPas').val() == '')
		{
			alert('No especificó la contraseña');
			$('.txtPas').focus();
			return;			
        }
        if($('.txtTel').val() == '')
		{
			alert('No especificó el telefono');
			$('.txtTel').focus();
			return;			
        }
        if($('.txtTel').val() == '')
		{
			alert('No especificó el telefono');
			$('.txtTel').focus();
			return;			
		}
		if($('.txtDate').val() == '')
		{
			alert('debe  ingresar fecha nacimiento');
			$('.txtDate').focus();
			return;			
        }
        
     
		if($('.select-css').val() == '')
		{
			alert('ingrese ciudad');
			$('.selectCiudad').focus();
			return;			
		}

        alert('Los datos ingresados fueron: \n' +
			$('.txtRutt').val() + '\n' +
			$('.txtNomb').val() + '\n' +
			$('.txtApellid').val()+ '\n' +
			$('.txtCorre').val() + '\n' +
			$('.txtPas').val() + '\n' +
			$('.txtTel').val() + '\n' +
			$('.txtDate').val() + '\n' +
			$('select[name="selectCiudad"] option:selected').text()+ '\n' +
			$('select[name="selectReg"] option:selected').text()+ '\n' +
			$('.select-css').val());	
    })
}
)