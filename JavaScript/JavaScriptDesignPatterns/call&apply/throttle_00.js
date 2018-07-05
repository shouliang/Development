/**
 * Created by shouliang on 2016/5/10.
 */
// 函数节流
var throttle = function (fn, interval) {
    var _self = fn;
    var timer;
    var firstTime = true;

    return function () {
        var args = arguments;
        var _me = this;

        if (firstTime) {
            _self.apply(_me, args);
            return firstTime = false;
        }

        if (timer) {
            return false;
        }

        timer = setTimeout(function () {
            clearTimeout(timer);
            timer = null;
            _self.apply(_me, args);
        }, interval || 500)
    }
}

// 分时函数
var timeChunk = function (ary, fn, count) {
    var obj;
    var t;
    var len = ary.length;

    var start = function () {
        for (var i = 0; i < Math.min(count || 1, ary.length); i++) {
            var obj = ary.shift();
            fn(obj);
        }
    }

    return function(){
        t = setInterval(function(){
            if( ary.length ===0){
                return clearInterval(t);
            }
            start();
        },200)
    }
}