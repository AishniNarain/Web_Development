let string = ""

let buttons = document.querySelectorAll(".button");

Array.from(buttons).forEach((td)=>{
    td.addEventListener('click', (e) => {
        console.log(e.target)
        if(e.target.innerHTML == "="){
            string = eval(string);
            document.getElementById("input").innerHTML = string;
        }
        else if(e.target.innerHTML == "C"){
            string = " ";
            document.getElementById("input").innerHTML = string;
        }
        else{
            string = string + e.target.innerHTML;
            console.log(string)
            document.getElementById("input").innerHTML = string;
        }
    })
})





