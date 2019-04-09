const https = require('https');
const fs = require('fs');

let options = {
    key:fs.readFileSync('./keys/server.key'),
    cert:fs.readFileSync('./keys/server.crt')
};

https.createServer(options,(req,res)=>{
    res.writeHead(200);
    res.end('Hello world\n');
}).listen(8000);