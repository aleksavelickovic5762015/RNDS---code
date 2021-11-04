import time
import socket


import caller

HOST = '192.168.43.22'  #192.168.0.58 192.168.0.58-mine  172.22.53.87-andrea
PORT = 8081    #8888

SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCK.connect((HOST, PORT))



id='2'


while True:

    if caller.get_user_flag(id)==1 and caller.get_user_door_status(id)==1 and caller.get_user_door_status(id)==1:
        print("sending: voldown")
        SOCK.sendall("voldown 3".encode())
    else:
        print("no one is disturbing")
    time.sleep(5)

    '''inp = input("type in 1/2/3/4/5")
    if(inp == '1'):
        print("sending: play ")
        SOCK.sendall("play".encode())
    elif(inp == '2'):
        print("sending: pause ")
        SOCK.sendall("pause".encode())
    elif(inp == '3'):
        print("sending: stop ")
        SOCK.sendall("stop".encode())
    elif (inp == '4'):
        print("sending: volup ")
        SOCK.sendall("volup".encode())
    elif (inp == '5'):
        print("sending: voldown ")
        SOCK.sendall("voldown".encode())'''