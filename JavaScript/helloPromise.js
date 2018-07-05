/*
 var fs = require('fs');
 fs.readFile('./package.json',function (err, data) {
 if (err) throw err;
 console.log(data.toString());
 });
 */

/*var fs = require("fs");

function hello(file) {
    return new Promise(function (reslove, reject) {
        fs.readFile(file, function (err, data) {
            if (err) {
                reject(err);
            } else {
                reslove(data);
            }
        })
    });
}

hello('./package.json')
    .then(function (data) {
        console.log('promise result is:' + data);
    })
    .catch(function (err) {
        console.log(err);
    })*/

// function doubleUp(value) {
//     return value * 2;
// }
// function increment(value) {
//     return value + 1;
// }
// function output(value) {
//     console.log(value);// => (1 + 1) * 2
// }
//
// var promise = Promise.resolve(1);
// promise
//     .then(increment)
//     .then(doubleUp)
//     .then(output)
//     .catch(function(error){
//         // promise chain中出现异常的时候会被调用
//         console.error(error);
//     });

var fs = require("fs");

function hello(file) {
    return new Promise(function (reslove, reject) {
        fs.readFile(file, function (err, data) {
            if (err) {
                reject(err);
            } else {
                reslove(data);
            }
        })
    });
}

hello('./package.json').then(function(data){
    console.log('way 1:\n')
    return new Promise(function(resolve, reject){
        console.log('promise result = ' + data)
        resolve(data)
    });
}).then(function(data){
    return new Promise(function(resolve, reject){
        resolve('1')
    });
}).then(function(data){
    console.log(data)

    return new Promise(function(resolve, reject){
        reject(new Error('reject with custom err'))
    });
}).catch(function(err) {
    console.log(err)
})


