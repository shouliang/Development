const fs = require('fs');
const tls = require('tls');

let options = {
    key:fs.readFileSync('./keys_02/server.pem'),
    cert: fs.readFileSync('./keys_02/server-cert.pem'),
    ca:[fs.readFileSync('./keys_02/client-cert.pem')],
    requestCert: true
};

let server = tls.createServer(options, (clearTextStream)=>{
    let authorized = clearTextStream.authorized? 'authorized': 'unauthorized';
    console.log('Connected:',authorized);
    clearTextStream.write('Welcome!\n');
    clearTextStream.setEncoding('utf8');
    clearTextStream.pipe(clearTextStream);
});

server.listen(8000,()=>{
    console.log('Server listening');
});