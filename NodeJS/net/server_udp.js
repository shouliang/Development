const dgram = require('dgram');
const server = dgram.createSocket('udp4');
server.on('message',(msg,addressInfo)=>{
    console.log(addressInfo);
    console.log(msg.toString());
    const data = Buffer.from('from server');
    server.send(data,addressInfo.port);
});

server.bind(3000,()=>{
    console.log('server is on', server.address());
})