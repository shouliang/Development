let tls = require('tls');
let fs = require('fs');

let options = {
    key: fs.readFileSync('./keys/client.key'),
    cert: fs.readFileSync('./keys/client.crt'),
    ca: [fs.readFileSync('./keys/ca.crt')]
};

let stream = tls.connect(8000, options, function () {
    console.log('client connected', stream.authorized ? 'authorized' : 'unauthorized');
    process.stdin.pipe(stream);
});

stream.setEncoding('utf8');
stream.on('data', function (data) {
    console.log(data);
});

stream.on('end', function () {
    //server.close();
});

stream.on('error', function (err) {
    console.log(err);
});

// let tls = require('tls');
// let os = require('os');
// let fs = require('fs');

// let options = {
//     key: fs.readFileSync('client.pem'),
//     cert: fs.readFileSync('client-cert.pem'),
//     ca: [fs.readFileSync('server-cert.pem')],
//     rejectUnauthorized:false
// };

// let clearTextStream = tls.connect(8000, options, function () {
//     console.log('client connected', clearTextStream.authorized ? 'authorized' : 'unauthorized');
//     process.stdin.pipe(clearTextStream);
// });

// clearTextStream.setEncoding('utf8');
// clearTextStream.on('data', function (data) {
//     console.log(data);
// });