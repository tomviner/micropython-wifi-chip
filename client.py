import socket
import machine
import neopixel

def get():
    s = socket.socket()
    s.connect(socket.getaddrinfo('stark-oasis-75010.herokuapp.com', 80)[0][-1])
    s.send('GET / HTTP/1.0\r\n\r\n')
    print(s.recv(1000))

def neo():
    np = neopixel.NeoPixel(p, 8)
    np[1] = (0, 255, 0)
    np.write()
    np[0] = (255, 255, 0)
    np.write()
    np[6] = (255, 255, 0)
    np.write()

get()