var net = require('net');
var client = net.connect({ port: 8124 }, function () { //'connect' listener
    console.log('client connected');
    client.write('say hi from client');
});

client.on('data', (data) => {
    console.log('data from server:', data.toString());
    client.end();
});

client.on('end', () => {
    console.log('client disconnected');
});

