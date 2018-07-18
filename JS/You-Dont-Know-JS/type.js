/**
 * Created by 朱守亮 on 2017/5/2.
 */
console.log('typeof undefined === undefined ', typeof undefined === 'undefined');
console.log('typeof true === boolean ', typeof true === 'boolean');
console.log('typeof 42 === number ', typeof 42 === 'number');
console.log("typeof '42' === string ", typeof '42' === 'string');
console.log('typeof {life:42} === object ', typeof {life: 42} === 'object');
console.log('typeof Symbol === symbol ', typeof Symbol() === 'symbol');

// undefined、boolean、number、string、object、symbol typeof之后均有同名的字符串值与之对应，而null 是个意外，typeof之后返回的是object
console.log('typeof null is ', typeof null);

// 判断null
let nulltest = null;
(!nulltest && typeof nulltest === 'object');

// 函数不仅是对象，还可以拥有数学
console.log('typeof function a(){} is ', typeof function a() {
});

// 数组也是对象
typeof [1, 2, 3] === 'object';

// 字符串反转 先转换成数组，利用数组的reverse
console.log('abcdef'.split('').reverse().join(''));

// js中字符串是不可变的，而数组是可变的,字符串不可变是指字符串的成员函数不会改变其原始值，而是创建并返回一个新的字符串
let originStr = 'abcdef';
let upperStr = originStr.toUpperCase();
originStr === upperStr; // false

console.log(' 0.1 + 0.2 === 0.3  is ', 0.1 + 0.2 === 0.3); // false
console.log(' numbersCloseEnoughToEqual(0.1 , 0.2 ) === 0.3  is ', numbersCloseEnoughToEqual(0.1, 0.2) === 0.3); // true

// 机器精度 machine epsilon,对js的数字来说，通常是 2^-52 (2.220446049250313e-16),Number.EPSILON用来比较两个数字是否相等(在指定的误差范围内)
function numbersCloseEnoughToEqual(n1, n2) {
    return Math.abs(n1 - n2) < Number.EPSILON;
}

// js中没有真正意义上的整数，“整数”就是没有小数的十进制数，所以42.00等同于“整数”42
console.log('42.00 is Integer is ', Number.isInteger(42.00));

// void运算符 返回的结果为undefined
console.log('void 0 is ', void 0);

// es6使用Number.isNaN来检测
console.log(" 4 / 'foo' is NaN is ", Number.isNaN(4 / 'foo'));

// NaN表示Not a number,但是其本身有是number类型的
console.log('typeof NaN is ', typeof  NaN);

// NaN是js中唯一一个不等于自身的值
console.log("  5 !== 5 is", 5 !== 5);
console.log("  abc !== abc is", 'abc' !== 'abc');
console.log("  NaN !== NaN is", NaN !== NaN);

let maxValue = Number.MAX_VALUE;
console.log(maxValue);
console.log(maxValue + maxValue);

// 0 === -0
console.log(1 / 0);  // -Infinity
console.log(-1 / 0); //  Infinity
0 / -3 === -0;
0 === -0; // true

// 判断-0
function isNegZero(n) {
    n = Number(n);
    return ( n === 0) && (1 / n === -Infinity);
}

// 值和引用 简单值总是通过值复制的方式来赋值
let a = 2;
let b = a;
b++;
console.log('a is ', a);
console.log('b is ', b);

// 复合值 对象(包括数组和封装对象)和函数，则总是通过引用复制的方式来赋值
let c = [1, 2, 3];
let d = c;
d.push(4);
console.log('c is ', c);
console.log('d is ', d);

let e = [1, 2, 3];
let f = e;
console.log('e is ', e);
console.log('f is ', f);

// then
f = [4, 5, 6];
console.log('e is ', e);0
console.log('f is ', f);

function foo(x) {
    x.push(4);
    x = [4, 5, 6];
    x.push(7);
}

let x = [1, 2, 3];
foo(x);
console.log('x is ', x);
