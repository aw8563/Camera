import io
import socket
import struct
import time
import picamera

client_socket = socket.socket()
client_socket.connect(("192.168.1.105", 5000))

connection = client_socket.makefile('wb')

try:
    camera = picamera.PiCamera()
    camera.resolution = (400,400)
    
    camera.start_preview()
    time.sleep(2)

    stream = io.BytesIO()
    startTime = time.time()
    
    for foo in camera.capture_continuous(stream, 'jpeg'):
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()

        stream.seek(0)
        stream.truncate()

    connection.write(struct.pack('<L', 0))

finally:
    connection.close()
    client_socket.close()



