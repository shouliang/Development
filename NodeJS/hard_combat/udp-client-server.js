const dgram = require('dgram');
const fs = require('fs');
let port = 41230;
let defaultSize = 16;

if (process.argv[2] === 'client') {
    new Client(process.argv[3]);
} else {
    new Server();
}

function Client(remoteIP) {
    let inStream = fs.createReadStream(__filename);
    let socket = dgram.createSocket('udp4');

    inStream.on('readable', () => {
        sendData();
    });

    function sendData() {
        let message = inStream.read(defaultSize);

        if (!message) {
            return socket.unref();
        }

        socket.send(message, 0, message.length, port, remoteIP),
            (err, bytes) => {
                if(err) {
                    console.log('send msg err', err);
                }
                sendData();
            }
    }

};

function Server() {
    let socket = dgram.createSocket('udp4');

    socket.on('message', (msg,rinfo) => {
        process.stdout.write(msg.toString());
    });

    socket.on('listening', () => {
        console.log('Server ready:', socket.address());
    });

    socket.bind(port);
};