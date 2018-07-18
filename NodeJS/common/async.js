/**
 * Created by shouliang on 2016/3/30.
 */
var async = require('async');

/* auto处理有依赖关系的多个任务的执行
 * auto(tasks,[concurrency],[callback]),此callback(err,results)可获取所有task的回调值
 * callback(err,data1,data2,...)以多参数的形式传递值，如：callback(null, 'data', 'converted to array')
 * callback(err, results),第一个为错误对象,results.方法名，可获取依赖关系的函数传递过来的值
 */
async.auto({
    getData: function(callback){
        callback(null, 'data', 'converted to array');
    },
    makeFolder: function(callback){
        callback(null, 'folder');
    },
    writeFile: ['getData', 'makeFolder', function(callback, results){
        callback(null, 'filename');
    }],
    emailLink: ['writeFile', function(callback, results){
        callback(null, {'file':results.writeFile, 'email':'user@example.com'});
    }]
}, function(err, results) {
    console.log('err = ', err);
    console.log('results = ', results);
});
