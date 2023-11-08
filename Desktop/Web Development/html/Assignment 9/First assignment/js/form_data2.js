// Using arrays

function getData(){
    event.preventDefault()
    let input = document.getElementsByName('arr')
    
    for(let i=0;i<input.length;i++){
        let array = []
        let a = input[i];
        console.log(`array[${i}].value = ${a.value}`);
    }

    

}

