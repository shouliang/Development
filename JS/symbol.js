/**
 * Created by 朱守亮 on 2017/3/24.
 */
// Symbol值通过Symbol函数生成，Symbol类型是独一无二的
let s = Symbol();
console.log('typeof s is ',typeof s); // "symbol"类型

// Symbol函数的参数只是描述，方便在控制台显示
let s1 = Symbol('foo');
let s2 = Symbol('bar');

console.log('s1 is ',s1);
console.log('s2 is ',s2);

// Symbol函数的参数是一个对象，则会调用该对象的toString方法，将其转为字符串
const obj = {
    toString() {
        return 'abc';
    }
};
const sym = Symbol(obj);
console.log('sym is ',sym);

// Symbol函数的参数只是表示对当前Symbol值的描述，因此相同参数的Symbol函数的返回值是不相等的
let s3 = Symbol();
let s4 = Symbol();
console.log('s3 === s4 is ', s3 === s4);

let s5 = Symbol('foo');
let s6 = Symbol('foo');
console.log('s5 === s6 is ', s5 === s6);

// Symbol可以显示转换成字符串
let s7 = Symbol('My symbol');
console.log('String(s7) is ',String(s7));
console.log('s7.toString() is ',s7.toString());

// Symbol也可以转换成布尔值
let s8 = Symbol();
if(s8){
    console.log('s8 is ', !!s8);
}

// 作为属性名的Symbol
let mySymbol = Symbol();
let a = {};
a[mySymbol] ='hello';
console.log('a[mySymbol] is ',a[mySymbol]);

// 通过Object.getOwnPropertySymbols获得成员属性
let objSym={};

let propA= Symbol('a');
let propB= Symbol('b');

objSym[propA] ='Hello';
objSym[propB] ='World';

let objectSymblos = Object.getOwnPropertySymbols(objSym);
console.log('objectSymblos is ',objectSymblos);

// Reflect.ownKeys返回所有类型的键名，包括Symbol键名
let objSym2 = {
    [Symbol('my_key')]:1,
    enum:2,
    nonEnum:3
};

console.log('objSym2 keys are ',Reflect.ownKeys(objSym2));

// Symbol.for
console.log(`Symbol.for('foo') === Symbol.for('foo') is `, Symbol.for('foo') === Symbol.for('foo'));
console.log(`Symbol('foo') === Symbol('foo') is `, Symbol('foo') === Symbol('foo'));

// Symbol.keyFor
let syb1 = Symbol.for('foo');
Symbol.keyFor(syb1);
console.log(`Symbol.keyFor(syb1) is `,Symbol.keyFor(syb1));
