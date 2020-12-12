function toggle() {

    inputs = document.getElementsByClassName("check-box-word");
    
    for (var i = 0; i < inputs.length; i++){
        if (inputs[i].checked){
            inputs[i].checked = false;
        }
        else {
            inputs[i].checked = true;
        }
    }

}
function check_email() {
    var email = document.getElementsByClassName("email-sign-up").login;
    var password = document.getElementsByClassName("password-sign-up").password;
    var agree = document.getElementsByClassName("terms-agree")[0].checked
    if (email.checkValidity() && password.checkValidity() && agree) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                document.getElementById("status").innerHTML = this.responseText;
                if (this.responseText == "Status - The message was sent"){
                    document.getElementsByClassName("verification")[0].style.display = "block";

                    document.getElementsByClassName("email-sign-up")[0].setAttribute("readonly", "readonly");
                    document.getElementsByClassName("password-sign-up")[0].setAttribute("readonly", "readonly");
                    document.getElementById("terms-agree").setAttribute("disabled", "disabled");
                    document.getElementById("sign-up-btn-first").setAttribute("disabled", "disabled");
                }
            }
        }
        xhr.open('POST', '/user-enter/verify_email', true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        xhr.send("email=" + email.value + "&password=" + password.value);
    }
}

function check_code() {
    var code = document.getElementById("code").value;
    if (code.length == 4) {
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                if (this.responseText == "Successful registration") {
                    window.location.replace("/user-enter/sign_in");
                }
                else {
                    document.getElementById("status").innerHTML = this.responseText;
                }
            }
        }
        xhr.open('POST', '/user-enter/verify_code', true);
        xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        xhr.send("code=" + code + "&email=" + document.getElementById("login").value);
    }
    else {
        document.getElementById("status").innerHTML = "4 значное число";
    }
}