/**
 * Created by shouliang on 2016/5/9.
 */

var func = function (a, b, c) {
    console.log([a,b,c]);
}
func.apply(null,[1,2,3]);

var func = function(a,b,c) {
    console.log([a,b,c]);
}
func.call(null,1,2,3); //传入的第一个参数为null,函数体内的this会指向默认的宿主对象

