export default function(){
    console.log("Hello");
}

let message = "ES6 Modules";

function user(name){
    return (`Hello ${name}`);
}

// class test{
//     constructor() {
//         console.log("Constructor method");
//     }
// }

// export { message, user, test};
export {message, user}

function user1(){
    return `Hello`;
}

export {user1};