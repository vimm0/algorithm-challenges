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


// Promises
// (callback hell):

func1(function (value1) {
    func2(value1, function (value2) {
        func3(value2, function (value3) {
            func4(value3, function (value4) {
                func5(value4, function (value5) {
                    // Do something with value 5
                });
            });
        });
    });
});

// Into vertical code:

func1(value1)
    .then(func2)
    .then(func3)
    .then(func4)
    .then(func5, value5 => {
        // Do something with value 5
    });

new Promise((resolve, reject) =>
    reject(new Error('Failed to fulfill Promise')))
    .catch(reason => console.log(reason));

let urls = [
    '/api/commits',
    '/api/issues/opened',
    '/api/issues/assigned',
    '/api/issues/completed',
    '/api/issues/comments',
];

let promises = urls.map((url) => {
    return new Promise((resolve, reject) => {
        $.ajax({url: url})
            .done((data) => {
                resolve(data);
            });
    });
});

Promise.all(promises)
    .then((results) => {
        // Do something with results of all our promises
    })

// Generator
function* sillyGenerator() {
    yield 1;
    yield 2;
    yield 3;
    yield 4;
}

var generator = sillyGenerator();
console.log(generator.next()); // { value: 1, done: false }
console.log(generator.next()); // { value: 2, done: false }
console.log(generator.next()); // { value: 3, done: false }
console.log(generator.next()); // { value: 4, done: false }