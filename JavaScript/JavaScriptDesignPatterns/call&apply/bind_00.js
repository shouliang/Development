/**
 * Created by shouliang on 2016/5/9.
 */
Function.prototype.bind = function () {
    var self = this;
    var context = [].shift.call(arguments);
    var args = [].slice.call(arguments);

    return function () {
        return self.apply(context, [].concat.call(args, [].slice.call(arguments)));
    }
}

var obj = {
    name: 'sven'
}

var func = function (a, b, c, d) {
    console.log(this.name);
    console.log([a, b, c, d]);
}.bind(obj, 1, 2);

func(3, 4);

// 借用其他对象
var A = function (name) {
    this.name = name;
}

var B = function () {
    A.apply(this, arguments)
}

B.prototype.getName = function () {
    return this.name;
}

var b = new B('sven');
console.log(b.getName());
