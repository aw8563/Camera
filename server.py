import socket
import time
import picamera

import io

camera = picamera.PiCamera()
camera.resolution = (512,512)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '192.168.1.114'
    port = 5000

    s.bind((ip,port))
    s.listen(1)

    while True:
        client, address = s.accept()
        while (True):
            try:
                sendData(client)
            except Exception as error:
                print(error)
                print("socket disconnected")
                client.close()
                break
        
    s.shutdown(1)
    s.close()
def sendData(socket):
    stream = io.BytesIO()

    for _ in camera.capture_continuous(stream, format='jpeg'):
        
        
        size = stream.tell()
        stream.seek(0)
        socket.send(stream.read())

        stream.seek(0)
        stream.truncate()
        print("data sent! [%d]"%size)




if __name__ == '__main__':
    main()
