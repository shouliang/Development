/**
 * Created by shouliang on 2016/5/10.
 */
var isString = function (obj) {
    return Object.prototype.toString.call(obj) === '[object String]';
}

var isArray = function (obj) {
    return Object.prototype.toString.call(obj) === '[object Array]';
}

var isNumber = function (obj) {
    return Object.prototype.toString.call(obj) === '[object Number]';
}

console.log(isString('str'));
console.log(isArray([]));
console.log(isNumber(8));


// 改进1
var isType = function (type) {
    return function (obj) {
        return Object.prototype.toString.call(obj) === '[object ' + type + ']';
    }
}

var isString = isType('String');
var isArray = isType('Array');
var isNumber = isType('Number');

console.log(isString('str'));
console.log(isArray([]));
console.log(isNumber(8));


// 改进2 批量注册函数
var Type = {};

for( var i = 0, type; type = ['String','Array','Number'][i++];){
    (function (type) {
        Type['is'+ type] = function(obj){
            return Object.prototype.toString.call(obj) === '[object ' + type + ']';
        }
    })( type)
};

console.log(isString('str'));
console.log(isArray([]));
console.log(isNumber(8));

