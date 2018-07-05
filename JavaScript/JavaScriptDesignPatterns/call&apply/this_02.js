/**
 * Created by shouliang on 2016/5/9.
 */
var obj1 = {
    name: 'sven',
    getName: function() {
        return this.name;
    }
}

var obj2 = {
    name: 'anne'
}

console.log( obj1.getName() );
console.log( obj1.getName.call( obj2));




var obj = {
    name: 'sven',
    getName: function() {
        return this.name;
    }
}
console.log( obj.getName() );

var getName = obj.getName;
console.log( getName());

