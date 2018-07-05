/**
 * Created by shouliang on 2016/5/9.
 */
var MyClass = function() {
    this.name = 'sven';
}
var obj = new MyClass();
console.log( obj.name );


var MyClass = function() {
    this.name = 'sven';
    return {
        name :'anne'
    }
}
var obj = new MyClass();
console.log( obj.name);


var MyClass = function () {
    this.name = 'sven';
    return 'anne';
}
var obj = new MyClass();
console.log( obj.name );



