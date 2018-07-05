/**
 * Created by shouliang on 2016/5/9.
 */
var func = function() {
    var a = 1;
    console.log(a);
}

func();

//console.log(a);

var func= function () {
    var a = 1;
    return function() {
        a++;
        console.log(a);
    }
}

var f = func();
f();
f();
f();
f();



