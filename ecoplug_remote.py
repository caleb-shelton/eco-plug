import serial
from datetime import datetime
import socket

# Start a serial connection on port 'COM3' with a baud rate of 115200
ser1 = serial.Serial('COM3', 115200)

# Opens a server with the device's ip and listens for incoming data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.43.94', 1339))
s.listen(1)

# Accepts any devices trying to connect
print('listening..')
conn, addr = s.accept()
print('connected')

# Used for decoding data in twos complement format which is sent over networks
def twoscomplement_to_unsigned(i):
    return i % 256

# Loop forever, receiving data from connected clients.
# If string 's' is received then send another 's' to the Arduino
# over serial connection defined above.
while True:
    try:
        data = conn.recv(3000)
        result = bytes(map(twoscomplement_to_unsigned, data))
        print('decoded: ', result)
        message = data.decode('utf-8')
        print(message)
        if 's' in message:
            print('s found')
            ser1.write('s'.encode())
            print('sent to arduino')
    except:
        print('error')
        pass
