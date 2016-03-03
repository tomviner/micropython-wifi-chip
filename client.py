"""
To paste this to the board:
  - do a regex replace s/([;:])\n    /\1 /
  - copy
  - pasta in the picocom shell!
"""
import socket
import machine
import neopixel
import json

def get():
    s = socket.socket();
    s.connect(socket.getaddrinfo('stark-oasis-75010.herokuapp.com', 80)[0][-1]);
    s.send('GET / HTTP/1.0\r\n');
    s.send('Host: stark-oasis-75010.herokuapp.com\r\n');
    s.send('\r\n');
    res = s.recv(1000);
    hds, body = res.split('\r\n\r\n');
    data = json.loads(body);
    print(data);
    return data

p = machine.Pin(4, machine.Pin.OUT)
np = neopixel.NeoPixel(p, 8)
data = get()
[np.__setitem__(i, d) for i,d in enumerate(data)]
np.write()
