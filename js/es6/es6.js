// Destructuring

// Destructuring Arrays
var arr = [1, 2, 3, 4];
var a = arr[0];
var b = arr[1];
var c = arr[2];
var d = arr[3];

let [a, b, c, d] = [1, 2, 3, 4];

console.log(a); // 1
console.log(b); // 2

// Destructuring Objects
var luke = {occupation: 'jedi', father: 'anakin'};
var occupation = luke.occupation; // 'jedi'
var father = luke.father; // 'anakin'
let luke = {occupation: 'jedi', father: 'anakin'};
let {occupation, father} = luke;

console.log(occupation); // 'jedi'
console.log(father); // 'anakin'


// Exporting in CommonJS
module.exports = 1;
module.exports = {foo: 'bar'};
module.exports = ['foo', 'bar'];
module.exports = function bar() {
};

// Exporting in ES6
export let name = 'David';
export let age = 25;​​

// exporting a list of objects:

function sumTwo(a, b) {
    return a + b;
}

function sumThree(a, b, c) {
    return a + b + c;
}

export {sumTwo, sumThree};

// export functions, objects and values by simply export keyword
export function sumTwo(a, b) {
    return a + b;
}

export function sumThree(a, b, c) {
    return a + b + c;
}

// export default bindings:

function sumTwo(a, b) {
    return a + b;
}

function sumThree(a, b, c) {
    return a + b + c;
}

let api = {
    sumTwo,
    sumThree
};

export default api;

/* Which is the same as
 * export { api as default };
 */

// Importing in ES6

// import 'underscore';
// import {sumTwo, sumThree} from 'math/addition'; // Similar to Python

//  rename the named imports:
// import {
//     sumTwo as addTwoNumbers,
//     sumThree as sumThreeNumbers
// } from 'math/addition';

// import all the things (also called namespace import):
// import * as util from 'math/addition';

// import a list of values from a module:
// import * as additionUtil from 'math/addition';
// const { sumTwo, sumThree } = additionUtil;