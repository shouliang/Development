const https = require('https');
const fs = require('fs');

let options = {
    hostname: 'localhost',
    port: 8000,
    path: '/',
    method: 'GET',
    key: fs.readFileSync('./keys/client.key'),
    cert: fs.readFileSync('./keys/client.crt'),
    ca: fs.readFileSync('./keys/ca.crt'),
    rejectUnauthorized: false
};

options.agent = new https.Agent(options);

let req = https.request(options, (res) => {
    res.setEncoding('utf-8');
    res.on('data', (data) => {
        console.log(data);
    });
});
req.end();

req.on('error', (error) => {
    console.log(error);
})