var socket = io.connect('http://127.0.0.1:5000');

socket.on('connect', function() {
    socket.send('I am now connected!');

    socket.on('message', function(msg) {
        alert(msg);
    });
});

