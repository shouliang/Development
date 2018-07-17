/**
 * Created by zhushouliang on 16/7/19.
 */
var fs = require('fs');

var rs = fs.createReadStream('./test1.txt');

var ws = fs.createWriteStream('./test2.txt');

rs.on('end', function() {
    console.log('read test1.txt successfully');
});

ws.on('finish', function() {
    console.log('write test2.txt successfully');
})

rs.pipe(ws);