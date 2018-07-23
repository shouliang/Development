const tls = require('tls');
const os = require('os');
const fs = require('fs');

let options = {
    key: fs.readFileSync('./keys_02/client.pem'),
    cert: fs.readFileSync('./keys_02/client-cert.pem'),
    ca: [fs.readFileSync('./keys_02/server-cert.pem')],
    servername: os.hostname()
};

let clearTextStream = tls.connect(8000, options, function () {
    console.log('client connected', clearTextStream.authorized ? 'authorized' : 'unauthorized');
    process.stdin.pipe(clearTextStream);
});

clearTextStream.setEncoding('utf8');
clearTextStream.on('data', function (data) {
    console.log(data);
});