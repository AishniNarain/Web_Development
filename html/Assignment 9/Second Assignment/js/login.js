function CheckData(){
    var email = document.getElementById('email').value;
    var password = document.getElementById('pwd').value;


    let getemail = localStorage.getItem('email');
    let getpassword = localStorage.getItem('password');

    if(email == getemail){
        if(password == getpassword){
            alert("Login Successful");
        }
        else{
            alert("Wrong password");
        }
    }
    else{
        alert("Login Fail");
    }
}