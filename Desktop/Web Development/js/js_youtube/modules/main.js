// import {default as show} from "./library.js"
import show, { message, user } from "./library.js"

show();

// import { message , user as u1, test} from "./library.js";
// import * as all from "./library.js"

// console.log(all.message);
// console.log(all.user("Aishni"));

console.log(message);
console.log(user("Aishni"));

// let t = new all.test();

import {user1} from "./bridge.js";

console.log(user1());
// document.body.innerHTML = message;
// document.body.innerHTML = user("Aishni");