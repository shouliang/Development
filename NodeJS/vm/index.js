// const util = require('util');
// const vm = require('vm');
// const script = new vm.Script('glovalVar +=1; anotherGlobalVar = 1 ;');

// const sandbox = { glovalVar: 1 };

// const contextifiedSandox = vm.createContext(sandbox);

// const result = script.runInContext(contextifiedSandox);

// console.log(`sandbox === contextifiedSandox ? ${sandbox === contextifiedSandox}`);

// console.log(`sanbox: ${util.inspect(sandbox)}`);

// console.log(`result: ${util.inspect(result)}`);

// ----------------------------------

// const util = require('util');
// const vm = require('vm');

// const sandbox = {globalVar: 1, setTimeout: setTimeout, cb: function(result) {
//     console.log(result);
// }};
// vm.createContext(sandbox);
// const script = new vm.Script(`
//     setTimeout(function(){
//         globalVar++;
//         cb("async result");
//     }, 1000);
// `,{});
// script.runInContext(sandbox);
// console.log(`globalVar: ${sandbox.globalVar}`);
// // globalVar: 1
// // async result


// ----------------------------------
// const util = require('util');
// const vm = require('vm');
// const sandbox = {};
// const contextifiedSandbox = vm.createContext(sandbox);
// const script = new vm.Script('while(true){}');
// const result = script.runInContext(contextifiedSandbox, {timeout: 1000});

// ----------------------------------
// const util = require('util');
// const vm = require('vm');

// const sandbox = {globalVar: 1, setTimeout: setTimeout, cb: function(result) {
//     console.log(result);
// }};
// vm.createContext(sandbox);
// const script = new vm.Script(`
//     setTimeout(function(){
//         globalVar++;
//         cb("async result");
//     }, 1000);
//     globalVar;
// `,{});
// const result = script.runInContext(sandbox, {timeout: 500});
// console.log(`result: ${result}`);
// // result: 1
// // async result

// ----------------------------------
// const util = require('util');
// const vm = require('vm');

// const sandbox = {};
// vm.createContext(sandbox);
// const script = new vm.Script(`
//     // sandbox 的 constructor 是外层的 Object 类
//     // Object 类的 constructor 是外层的 Function 类
//     const OutFunction = this.constructor.constructor;
//     // 于是, 利用外层的 Function 构造一个函数就可以得到外层的全局 this
//     const OutThis = (OutFunction('return this;'))();
//     // 得到 require
//     const require = OutThis.process.mainModule.require;
//     // 试试
//     require('fs');
// `,{});
// const result = script.runInContext(sandbox);
// console.log(result === require('fs'));
// // true


// ----------------------------------
var vm = require("vm");
 
var p = 5;
global.p = 11;
 
vm.runInThisContext("console.log('ok', p)");// 显示global下的11
vm.runInThisContext("console.log(global)"); // 显示global
 
console.log(p);// 显示5