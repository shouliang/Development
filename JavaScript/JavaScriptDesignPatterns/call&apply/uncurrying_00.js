/**
 * Created by shouliang on 2016/5/10.
 */
(function(){
    Array.prototype.push.call(arguments,4);
    console.log( arguments);
})(1,2,3);

// uncurrying实现方式之一
Function.prototype.uncurrying = function() {
    var self = this;
    return function() {
        var obj = Array.prototype.shift.call(arguments);
        return self.apply(obj, arguments);
    }
}

// 将Array.prototype.push 转化成通用的push函数
var push = Array.prototype.push.uncurrying();

(function(){
    push(arguments,4);
    console.log(arguments);
})(1,2,3);