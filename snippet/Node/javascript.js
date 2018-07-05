1.全局替换
（1）其实replace本身也可以实现这种功能的，但要通过正则的形式加个参数g，例如：
str.replace(/www.baidu.com/g,'www.phpernote.com');
或者：
str.replace(new RegExp('www.baidu.com','gm'),'www.phpernote.com');
将 str 字符中的 www.baidu.com 全部替换为 www.phpernote.com

（2）自己扩展js函数库，自创函数replaceall方法实现全局匹配并替换的功能。如下：
String.prototype.replaceall=function(s1,s2){
    return this.replace(new RegExp(s1,"gm"),s2);
}

2.node升级6.9.1之后，hasOwnProperty is not a function
options.hasOwnProperty('index') ->Object.prototype.hasOwnProperty.call(options,'index')

3.JavaScript获取当前时间的Unix时间戳：Math.round(new Date().getTime()/1000)，详见：http://tool.chinaz.com/Tools/unixtime.aspx

4.非ascii码的url编码：encodeURIComponent('海外婚礼首页列表');