///**
// * Created by shouliang on 2016/5/28.
// */
//var duck = {
//    duckSinging: function(){
//        console.log( '嘎嘎嘎' );
//    }
//};
//
//var chicken = {
//    duckSinging: function(){
//        console.log( '嘎嘎嘎' );
//    }
//};
//
//var choir = []; // 合唱团
//var joinChoir = function( animal ){
//    if ( animal && typeof animal.duckSinging === 'function' ){
//        choir.push( animal );
//        console.log( '恭喜加入合唱团' );
//        console.log( '合唱团已有成员数量:' + choir.length );
//    }
//};
//joinChoir( duck ); // 恭喜加入合唱团
//joinChoir( chicken ); // 恭喜加入合唱团
//
//
//
//var makeSound = function( animal ){
//    if ( animal instanceof Duck ){
//        console.log( '嘎嘎嘎' );
//    }else if ( animal instanceof Chicken ){
//        console.log( '咯咯咯' );
//    }
//};
//var Duck = function(){};
//var Chicken = function(){};
//makeSound( new Duck() ); // 嘎嘎嘎
//makeSound( new Chicken() ); // 咯咯咯
//
//
//下面是改写后的代码，首先我们把不变的部分隔离出来，那就是所有的动物都会发出叫声：
//var makeSound = function( animal ){
//    animal.sound();
//};
//
//然后把可变的部分各自封装起来，我们刚才谈到的多态性实际上指的是对象的多态性：
//var Duck = function(){}
//Duck.prototype.sound = function(){
//    console.log( '嘎嘎嘎' );
//};
//var Chicken = function(){}
//Chicken.prototype.sound = function(){
//    console.log( '咯咯咯' );
//};
//makeSound( new Duck() ); // 嘎嘎嘎
//makeSound( new Chicken() ); // 咯咯咯
//
//
//现在我们向鸭和鸡都发出“叫唤”的消息，它们接到消息后分别作出了不同的反应。如果有
//一天动物世界里又增加了一只狗，这时候只要简单地追加一些代码就可以了，而不用改动以前的
//makeSound 函数，如下所示：
//var Dog = function(){}
//Dog.prototype.sound = function(){
//    console.log( '汪汪汪' );
//};
//makeSound( new Dog() ); // 汪汪汪
//
//
//在许多语言的对象系统中，封装数据是由语法解析来实现的，这些语言也许提供了 private、
//public、 protected 等关键字来提供不同的访问权限。
//但 JavaScript 并没有提供对这些关键字的支持，我们只能依赖变量的作用域来实现封装特性，
//而且只能模拟出 public 和 private 这两种封装性。
//除了 ECMAScript 6 中提供的 let 之外，一般我们通过函数来创建作用域：
//var myObject = (function(){
//    var __name = 'sven'; // 私有（private）变量
//    return {
//        getName: function(){ // 公开（public）方法
//            return __name;
//        }
//    }
//})();
//console.log( myObject.getName() ); // 输出： sven
//console.log( myObject.__name ) // 输出： undefined
//
//
//封装的目的是将信息隐藏，封装应该被视为“任何形式的封装”，也就是说，封装不仅仅是
//隐藏数据，还包括隐藏实现细节、设计细节以及隐藏对象的类型等。
//从封装实现细节来讲，封装使得对象内部的变化对其他对象而言是透明的，也就是不可见的。
//对象对它自己的行为负责。其他对象或者用户都不关心它的内部实现。封装使得对象之间的耦合
//变松散，对象之间只通过暴露的 API 接口来通信。当我们修改一个对象时，可以随意地修改它的
//内部实现，只要对外的接口没有变化，就不会影响到程序的其他功能。
//
//
//
//事实上， JavaScript 中的根对象是 Object.prototype 对象。 Object.prototype 对象是一个空的
//对象。我们在 JavaScript 遇到的每个对象，实际上都是从 Object.prototype 对象克隆而来的，
//Object.prototype 对象就是它们的原型。比如下面的 obj1 对象和 obj2 对象：
//var obj1 = new Object();
//var obj2 = {};
//可以利用 ECMAScript 5 提供的 Object.getPrototypeOf 来查看这两个对象的原型：
//console.log( Object.getPrototypeOf( obj1 ) === Object.prototype ); // 输出： true
//console.log( Object.getPrototypeOf( obj2 ) === Object.prototype ); // 输出： true
//
//
//再来看看如何用 new 运算符从构造器中得到一个对象，下面的代码我们再熟悉不过了：
//function Person( name ){
//    this.name = name;
//};
//Person.prototype.getName = function(){
//    return this.name;
//};
//var a = new Person( 'sven' )
//console.log( a.name ); // 输出： sven
//console.log( a.getName() ); // 输出： sven
//console.log( Object.getPrototypeOf( a ) === Person.prototype ); // 输出： true
//
//
//再看这段代码执行的时候，引擎做了什么事情。
// 首先，尝试遍历对象 b 中的所有属性，但没有找到 name 这个属性。
//
// 查找 name 属性的请求被委托给对象 b 的构造器的原型，它被 b.__proto__ 记录着并且指向
//B.prototype，而 B.prototype 被设置为一个通过 new A()创建出来的对象。
// 在该对象中依然没有找到 name 属性，于是请求被继续委托给这个对象构造器的原型
//A.prototype。
// 在 A.prototype 中找到了 name 属性，并返回它的值。
//
//


//var a = new Object();
//console.log(a.__proto__ === Object.prototype);        //true
//
//
//
//当函数作为对象的方法被调用时， this 指向该对象：
//var obj = {
//    a: 1,
//    getA: function(){
//        alert ( this === obj ); // 输出： true
//        alert ( this.a ); // 输出: 1
//    }
//};
//obj.getA();
//
//
//
//当函数不作为对象的属性被调用时，也就是我们常说的普通函数方式，此时的 this 总是指
//向全局对象。在浏览器的 JavaScript 里，这个全局对象是 window 对象。
//window.name = 'globalName';
//var getName = function(){
//    return this.name;
//};
//console.log( getName() ); // 输出： globalName
//或者：
//window.name = 'globalName';
//var myObject = {
//    name: 'sven',
//    getName: function(){
//        return this.name;
//    }
//};
//var getName = myObject.getName;
//console.log( getName() ); // globalName
//
//
//跟普通的函数调用相比，用 Function.prototype.call 或 Function.prototype.apply 可以动态地
//改变传入函数的 this：
//var obj1 = {
//    name: 'sven',
//    getName: function(){
//        return this.name;
//    }
//};
//var obj2 = {
//    name: 'anne'
//};
//console.log( obj1.getName() ); // 输出: sven
//console.log( obj1.getName.call( obj2 ) ); // 输出： anne
//
//
//
//丢失的this
//这是一个经常遇到的问题，我们先看下面的代码：
//var obj = {
//    myName: 'sven',
//    getName: function(){
//        return this.myName;
//    }
//};
//console.log( obj.getName() ); // 输出： 'sven'
//var getName2 = obj.getName;
//console.log( getName2() ); // 输出： undefined
//当调用 obj.getName 时， getName 方法是作为 obj 对象的属性被调用的，根据 2.1.1 节提到的规
//律，此时的 this 指向 obj 对象，所以 obj.getName()输出'sven'。
//
//当用另外一个变量 getName2 来引用 obj.getName，并且调用 getName2 时，根据 2.1.2 节提到的
//规律，此时是普通函数调用方式， this 是指向全局 window 的，所以程序的执行结果是 undefined。