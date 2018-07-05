/**
 * Created by shouliang on 2016/5/11.
 */
var Singleton = function (name) {
    this.name = name;
    this.instance = null;
};

Singleton.prototype.getName = function () {
    console.log(this.name);
};

Singleton.getInstance = function (name) {
    if (!this.instance) {
        this.instance = new Singleton(name);
    }
    return this.instance;
};

var s1 = Singleton.getInstance('s1');
var s2 = Singleton.getInstance('s2');

console.log(s1 === s2);

/*
 这种方式相对简单，但有
 一个问题，就是增加了这个类的“不透明性”， Singleton 类的使用者必须知道这是一个单例类，
 跟以往通过 new XXX 的方式来获取对象不同，这里偏要使用 Singleton.getInstance 来获取对象。
 */

var CreateDiv = (function () {
    var instance;

    var CreateDiv = function (html) {
        if (instance) {
            return instance;
        }
        this.html = html;
        this.init();
        return instance = this;
    }

    CreateDiv.prototype.init = function () {

    }

    return CreateDiv;

})();

var a = new CreateDiv('shouliang1');
var b = new CreateDiv('shouliang2');

console.log(a === b);


// 使用代理实现单例
var CreateDiv = function (html) {
    this.html = html;
    this.init();
};

CreateDiv.prototype.init = function () {

};

var ProxySingletonCreateDiv = (function () {
    var instance;
    return function (html) {
        if (!instance) {
            instance = new CreateDiv(html);
        }

        return instance;
    }
})();

var s1 = new ProxySingletonCreateDiv("s1");
var s2 = new ProxySingletonCreateDiv("s2");

console.log(s1 === s2);