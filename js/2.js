let namaste_button = document.querySelector('button');
// namaste_button.addEventListener('click',showMsg);

// function showMsg(){
//     alert("Namaste World!");
// }

namaste_button.addEventListener('click',inputMsg);

function inputMsg(){
    let name = prompt("Enter a Student Name : ");
    namaste_button.textContent = "Roll No. 1 : " + name;
}
