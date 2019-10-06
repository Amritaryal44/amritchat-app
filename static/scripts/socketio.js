document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect('http://'+document.domain+':'+location.port); //connects to the socketio server
    let room = "Lounge";
    joinRoom("Lounge"); //User initially is joined to the Lounge Room

    socket.on('message', data => {
        const p = document.createElement('p');
        const span_username = document.createElement('span');
        const span_timestamp = document.createElement('span');
        const br = document.createElement('br');
        if (data.username) {
            span_username.innerHTML = data.username;
            span_timestamp.innerHTML = data.time_stamp;
            p.innerHTML = span_username.outerHTML+br.outerHTML+data.msg+br.outerHTML+span_timestamp.outerHTML;
            document.querySelector("#display-message-section").append(p);
        } else {
            printSysMsg(data.msg);
        }
    });

    /*
    socket.on('some-event', data => {
        console.log(data);
    });
    */
   document.querySelector('#user_message').addEventListener('keyup', function(event) {
       event.preventDefault();
       if (event.keyCode == 13) {
           document.querySelector('#send_message').click();
       }
   });

    document.querySelector('#send_message').onclick = function() {
        socket.send({'msg':document.querySelector('#user_message').value, 'username':username, 'room':room});
        document.querySelector('#user_message').value = "";
    }

    //Room  selection
    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = function() {
            let newRoom = p.innerHTML;
            if (newRoom == room) {
                msg = `You are already in ${room} room.`;
                printSysMsg(msg);
            } else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        }
    });
    
    function leaveRoom(room) {
        socket.emit('leave', {'username':username, 'room':room});
    } 

    function joinRoom(room) {
        socket.emit('join', {'username':username, 'room':room});
    }

    function printSysMsg(msg) {
        const p = document.createElement('p');
        p.innerHTML=msg;
        document.querySelector('#display-message-section').append(p);
    }
});