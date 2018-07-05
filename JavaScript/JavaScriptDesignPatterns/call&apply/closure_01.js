/**
 * Created by shouliang on 2016/5/9.
 */
var mult = function () {
    var a = 1;
    for (var i = 0, l = arguments.length; i < l; i++) {
        a = a * arguments[i];
    }
    return a;
}

console.log(mult(2, 3, 4));

// 优化1
var cache = {};
var mult = function () {
    var args = Array.prototype.join.call(arguments, ',');
    if (cache [args]) {
        return cache[args];
    }

    var a = 1;
    for (var i = 0, l = arguments.length; i < l; i++) {
        a = a * arguments[i];
    }

    return cache[args] = a;
}

console.log(mult(2, 3, 4));


// 优化2
var mult = (function () {
    var cache = {};
    return function () {
        var args = Array.prototype.join.call(arguments, ',');
        if (cache [args]) {
            return cache[args];
        }

        var a = 1;
        for (var i = 0, l = arguments.length; i < l; i++) {
            a = a * arguments[i];
        }

        return cache[args] = a;
    }
})();

console.log(mult(2, 3, 4));


// 优化3
var mult = (function(){
    var cache = {};
    var calculate = function(){
        var a = 1;
        for(var i= 0,l=arguments.length;i<l;i++){
            a = a * arguments[i];
        }
        return a;
    }

    return function(){
        var args = Array.prototype.join.call(arguments, ',');
        if (args in cache) {
            return cache[ args];
        }

        return cache [args] = calculate.apply(null, arguments);
    }

})();

mult(2,3,4);