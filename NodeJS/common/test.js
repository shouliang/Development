// let v1 = []
// let v2 = {};
// let v3 = {};

// function foo(v1, v2, v3)
// {
//     v1 = [1];
//     v2 = [2];
//     v3 = {a:3}
// }

// foo(v1, v2, v3);

// console.log(v1);   // []
// console.log(v2);   // {}
// console.log(v3.a); // undefined

// ------------------------------

// let c1 = {v:1};
// let c2 = c1;
// c2.v = 11;
// c2 = {v:2};
// console.log(c1.v); // 显示 11
// console.log(c2.v); // 显示 2


// ------------------------------

// let user = new Object();
// let admin = user;
// admin.name = "xiaoxiaozi";
// console.log(user.name); 

// admin = {name:'zhangsan'};
// console.log(user.name);
// ------------------------------

// function setName(obj){
// 	obj.name="zhangsan";
// 	obj=new Object();
// 	obj.name="lisi";
// }
// var obj=new Object();
// setName(obj);
// console.log(obj.name);
// //输出zhangsan

// ------------------------------
// let a = {
//     p: [1, 2]
// };
// let b = Object.assign({}, a);

// console.log('b === a is ', b === a);
// console.log('b.p === a.p', b.p === a.p);
// ------------------------------

// function deepClone(obj) {
//     return JSON.parse(JSON.stringify(obj));
// }

// function deepCopy(src) {
//     if (!src || typeof src !== 'object') {
//         throw new Error('error arguments');
//     }
//     let target = src.constructor === Array ? [] : {};
//     for (let i in src) {
//         if (typeof src[i] === 'object') {
//             target[i] = src[i].constructor === Array ? [] : {};
//             target[i] = deepCopy(src[i]);
//         } else {
//             target[i] = src[i];
//         }
//     }
//     return target;
// }

// let o1 = {
//     arr: [1, 2, 3],
//     obj: { key: 'value' },
//     func() {
//         return 1;
//     }
// };

// let o2 = deepClone(o1);
// let o3 = deepCopy(o1);
// console.log(o2); // => {arr: [1,2,3], obj: {key: 'value'}}
// console.log(o3);
// ------------------------------

// for (let i = 0; i < 3; i++) {
//     let i = 'abc';
//     console.log(i);
// }
// ------------------------------

// {
//     let a = 10;
//     var b = 1;
// }
// console.log('a = ', a);
// console.log('b = ', b);

// ------------------------------

// console.log(foo);
// var foo = 2;

// console.log(bar);
// let bar = 2;

// ------------------------------

let symbol1 = Symbol();
let symbol2 = Symbol();
console.log( symbol1=== symbol2);
console.log(typeof symbol1);

let myObject = {
    publicProperty: 'Value of myObject["publicProperty"]'
};
myObject[symbol1] = 'Value of myObject[symbol1]';
myObject[symbol2] = 'Value of myObject[symbol2]';

console.log(myObject);
console.log(myObject[symbol1]);

console.log('--------')
console.log(JSON.stringify(myObject));

for(let prop in myObject){
    console.log(prop, myObject[prop]);
}

console.log(Object.keys(myObject));
//console.log(myObject[Object.getOwnPropertySymbols(myObject)[0]]);
