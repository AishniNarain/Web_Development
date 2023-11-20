// Using getElementBy Id

function accessed_data(){
    event.preventDefault()
    let name = document.getElementById("name");
    let phone = document.getElementById("phno");
    let emailid = document.getElementById("email");
    let age = document.getElementById("age");

    console.log(`Name is : ${name.value} , Phone Number is : ${phone.value} , Email Id is : ${emailid.value} , Age is : ${age.value}`)

    name.value = "";
    phone.value = "";
    emailid.value = "";
    age.value = "";

}

//