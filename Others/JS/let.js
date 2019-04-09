/**
 * Created by 朱守亮 on 2017/3/27.
 */
// let声明的变量只在代码块中有效
{
    let a = 10;
    var b = 1;
}
//console.log('a is ', a); //ReferenceError: a is not defined
console.log('b is ', b);

// i通过var声明，在全局范围内有效,所以循环结束后i=10
var a = [];
for (var i = 0; i < 10; i++) {
    a[i] = function () {
        console.log(i);
    }
}
a[6]();

// let声明的变量只在代码块中有效
for (let i = 0; i < 10; i++) {
    a[i] = function () {
        console.log(i);
    }
}
a[6]();

for (let i = 0; i < 3; i++) {
    let i = 'abc';
    console.log(i);
}

// var命令发生变量提升的想象，即变量在声明之前使用，值为undefined
console.log(foo); // 输出undefined
var foo = 2;

// let命令不发生变量提升，所以变量bar必须先声明再使用，否则会抛出“ReferenceError: bar is not defined”的错误
//console.log(bar);
//let bar = 2;

var tmp = 123;
if (true) {
    // tmp = 'abc';
    // let tmp; // tmp变量被绑定到块级作用域，必须先声明再使用
}

// typeof在没有let之前是百分之百安全的
typeof xxx;

//typeof yyy;
//let yyy=1;

// let不允许在作用域内，重复声明同一个变量
function t() {
    let a = 10;
    // let a = 1;
    // var a =1;
}