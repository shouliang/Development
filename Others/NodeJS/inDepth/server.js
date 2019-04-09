const net = require('net');

const server = net.createServer((socket) => {
    socket.on('data', (data) => {
        console.log('data from client:', data.toString());
        socket.write('say hi from server');
    });

    socket.write("欢迎光临《深入浅出Node.js》\n");

    socket.on('end', () => {
        console.log('客户端连接断开');
    });
});

server.listen(8124, () => {
    console.log('server bound');
})