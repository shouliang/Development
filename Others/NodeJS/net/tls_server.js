const tls = require('tls');
const fs = require('fs');

let options = {
    key: fs.readFileSync('./keys/server.key'),
    cert: fs.readFileSync('./keys/server.crt'),
    ca:[fs.readFileSync('./keys/ca.crt')],
    requestCert: true
};

let server = tls.createServer(options, (stream)=>{
    consoel.log('sever connected', stream.authorized? 'authorized':'unauthorized');
    stream.write('welcome!\n');
    stream.setEncoding('utf8');
    stream.pipe(stream);
});

server.listen(8000,()=>{
    console.log('server bound');
});

// const fs = require('fs');
// const tls = require('tls');

// let options = {
//     key:fs.readFileSync('server.pem'),
//     cert: fs.readFileSync('server-cert.pem'),
//     ca:[fs.readFileSync('client-cert.pem')],
//     requestCert: true
// };

// let server = tls.createServer(options, (clearTextStream)=>{
//     let authorized = clearTextStream.authorized? 'authorized': 'unauthorized';
//     console.log('Connected:',authorized);
//     clearTextStream.write('Welcome!\n');
//     clearTextStream.setEncoding('utf8');
//     clearTextStream.pipe(clearTextStream);
// });

// server.listen(8000,()=>{
//     console.log('Server listening');
// });