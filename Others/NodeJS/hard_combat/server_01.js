const net = require('net');
let clients = 0;

let server = net.createServer((client) => {
    clients++;
    let clientId = clients;
    console.log('Client connected:', clientId);
     
    console.log('client is ',(client));

    client.write('Welcome client:' + clientId);
    client.pipe(client);

    client.on('end', () => {
        console.log('Client disconnected:', clientId);
    })
});

server.listen(8000, () => {
    console.log('Server started on port 8000');
})