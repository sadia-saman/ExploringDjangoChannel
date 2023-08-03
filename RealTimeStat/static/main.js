var socket = new WebSocket('ws://localhost:8000/ws/realtime/');

socket.onmessage = function (event) {
    var data = JSON.parse(event.data); 
    var value = data.value;
    var element = document.getElementById('app');
    if (element) {
        element.innerHTML = value;
    }
} 