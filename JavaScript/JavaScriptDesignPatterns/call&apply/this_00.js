/**
 * Created by shouliang on 2016/5/9.
 */
var obj = {
    a: 1,
    getA: function () {
        console.log(this === obj);
        console.log(this.a);
    }
}
obj.getA();

global.name = 'globalName';
var getName = function () {
    return this.name;
}
console.log(getName());

global.name = 'globalName';
var myObject = {
    name: 'sven',
    getName: function () {
        return this.name;
    }
}
var getName = myObject.getName;
console.log(getName());
