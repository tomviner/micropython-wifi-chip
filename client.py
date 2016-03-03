"""
To paste this to the board:
  - copy
  - in the picocom shell:
    - ctrl-e
    - pasta
    - ctrl-d
"""
import socket
import machine
import neopixel
import json
import time

def get():
    s = socket.socket()
    s.connect(socket.getaddrinfo('stark-oasis-75010.herokuapp.com', 80)[0][-1])
    s.send('GET /get HTTP/1.0\r\n')
    s.send('Host: stark-oasis-75010.herokuapp.com\r\n')
    s.send('\r\n')
    res = s.recv(1000)
    hds, body = res.split(b'\r\n\r\n', 1)
    data = json.loads(body)
    print(data)
    return data

on = [list((0, 0, 0)) for _ in range(8)]
off = [list((255, 255, 255)) for _ in range(8)]

p = machine.Pin(4, machine.Pin.OUT)
np = neopixel.NeoPixel(p, 8)
while 1:
    data = get()
    [np.__setitem__(i, d) for i,d in enumerate(data)]
    np.write()
    time.sleep(0.5)
