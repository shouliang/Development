exports.id = 'index';
module.exports = function(){};
console.log('In index', module);
const UTIL = require('./lib/util');
console.log('UTIL:',UTIL);

setImmediate(()=>{
    console.log('The index.js module object is now loaded!',module);
})