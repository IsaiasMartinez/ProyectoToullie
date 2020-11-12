$(function()
{
    
    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú- ';
    
    
    

                
    $('txtCorreo, .txtPass').keypress(function(e)
    {
        let caracter= String.fromCharCode(e.wich);
        if(numeros.indexOf(caracter)<0)
            return false;

    });

    $('.btnEnviar').click(function()
    {

        		
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
        
        alert('Los datos ingresados fueron: \n' +
			$('.txtCorre').val() + '\n' +
			$('.txtPas').val());	
    })
}
)