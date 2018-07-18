console.log('main starting'); 
var a = require('./a.js'); // --> 0
var b = require('./b.js');
console.log('in main, a.done=%j, b.done=%j', a.done, b.done);