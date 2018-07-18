// let fs = require('fs');
// fs.readFile('./names.txt',function(err,buf){
//     console.log(Buffer.isBuffer(buf));
// })

// ----------------------------------------
// let fs = require('fs');
// fs.readFile('./names.txt', function (err, buf) {
//     console.log(buf);
//     console.log(buf.toString());
//     console.log(buf.toString('ascii'));
// });

// ----------------------------------------
// let user = 'johnny';
// let pass = 'c-bad';
// let authstring = user + ':' + pass;
// let buf = new Buffer(authstring);
// console.log('buf is:');
// console.log(buf);

// let encoded = buf.toString('base64');
// console.log(encoded);

// ----------------------------------------

// const fs = require('fs');
// let mime = 'img/jpeg';
// let encoding = 'base64';
// let data = fs.readFileSync('./monkey.jpeg').toString(encoding);
// let uri = 'data:' + mime + ';' + encoding + ',' + data;

// let secondData = uri.split(',')[1];
// let buf = Buffer(secondData,encoding);
// fs.writeFileSync('./secondmonkey.jpeg',buf);

// console.log(uri);

// ----------------------------------------
// let fs = require('fs');
// // let rs = fs.createReadStream('test.md');
// let rs = fs.createReadStream('test.md',{highWaterMark: 11});
// rs.setEncoding('utf8');
// let data ='';
// rs.on('data',function(chunk){
//     data += chunk;
// });

// rs.on('end',function(){
//     console.log(data);
// })

// ----------------------------------------

const arr = new Uint16Array(2);
arr[0] = 5000;
arr[1] = 4000;

const buf1 = Buffer.from(arr);        // 拷贝了该 buffer
const buf2 = Buffer.from(arr.buffer); // 与该数组共享了内存

// 输出: <Buffer 88 a0>, 拷贝的 buffer只有两个元素,
// Buffer的实现基于TypedArray中Uint8Array，所以元素1和元素2都只能输出1个字节
console.log(buf1);

// 输出: <Buffer 88 13 a0 0f>
console.log(buf2);

arr[1] = 6000;
console.log(buf1); // 输出: <Buffer 88 a0>
console.log(buf2); // 输出: <Buffer 88 13 70 17>


// ----------------------------------------

// const readline = require('readline');
// const fs = require('fs');

// const rl = readline.createInterface({
//     input:fs.createReadStream('names.txt')
// })

// rl.on('line',(line)=>{
//     console.log(`Line from file: ${line}`);
// })

// ----------------------------------------