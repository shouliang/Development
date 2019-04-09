const dgram = require('dgram');
const client = dgram.createSocket('udp4');
const data = Buffer.from('from client');
client.send(data,3000);
client.on('message',(msg,addressInfo )=>{
    console.log(addressInfo);
    console.log(msg.toString());
    client.close();
})