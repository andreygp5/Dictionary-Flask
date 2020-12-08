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