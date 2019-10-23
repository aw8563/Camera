import socket
import time
import cv2
import io

from matplotlib import pyplot
from PIL import Image

def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
        time.sleep(0.0001)        
    return data


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '203.63.149.98'

port = 5000

s.connect((host, port))

pyplotImage = None

while (True):
    data = recvall(s)
    
    if (data):
        print("len = [%d]"%len(data))
        imgStream = io.BytesIO()
        imgStream.write(data)
        imgStream.seek(0)

        image = Image.open(imgStream)
        if not pyplotImage:
            pyplotImage = pyplot.imshow(image)
        else:
            pyplotImage.set_data(image)

        pyplot.pause(0.01)
        pyplot.draw()


    else:
        s.shutdown(1)
        s.close()
        print("connection lost")
        break

