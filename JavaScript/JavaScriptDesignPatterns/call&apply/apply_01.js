/**
 * Created by shouliang on 2016/5/9.
 */
var obj1 = {
    name:'sven'
}

var obj2 = {
    name:'anne'
}

global.name = 'global';

var getName = function() {
    console.log(this.name);
}

getName();
getName.call(obj1);
getName.call(obj2);
