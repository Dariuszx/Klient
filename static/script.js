var password_field = document.getElementById('password');
var username_field = document.getElementById('username');

password_field.addEventListener( 'keyup', check_login_form );
username_field.addEventListener( 'keyup', check_login_form );

function check_login_form() {

    var username = document.getElementById('username');
    var password = document.getElementById('password');

    var flag = false;

    var pass = password.value;
    var usr = username.value;

    if( usr.trim().length < 3 ) flag = true;
    if( pass.length < 3 ) flag = true;


    if( flag ) {
        var submit_button = document.getElementById('submit');
        submit_button.removeAttribute( 'enabled' )
        submit_button.setAttribute('disabled', 'disabled');
    } else {
        var submit_button = document.getElementById('submit');
        submit_button.removeAttribute('disabled')
        submit_button.setAttribute('enabled', 'enabled');
    }
}