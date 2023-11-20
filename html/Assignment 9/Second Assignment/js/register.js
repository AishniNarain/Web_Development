function saveData(){
let name = document.getElementById('name').value;
let phone = document.getElementById('phno').value;
let email = document.getElementById('email').value;
let password = document.getElementById('pwd').value;


// using setItem only
localStorage.setItem('name',name);
localStorage.setItem('phno',phone);
localStorage.setItem('email',email);
localStorage.setItem('password',password)

// let user_records = new Array();

// user_records = JSON.parse(localStorage.getItem("users"))?JSON.parse(localStorage.getItem("users")):[]

// if(user_records.some((data) => {
//     return data.email==email }))
// {
//     alert("Please do not enter duplicate data")
// }
// else{
//     user_records.push({
//         "name": name,
//         "phone" : phone,
//         "email" : email,
//         "pwd" : password
//     })
    
//     localStorage.setItem("users",JSON.stringify(user_records));
// }

}
