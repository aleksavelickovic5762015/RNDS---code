import socket
import caller
import time

SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SOCK.connect(("192.168.0.35", 20000))


id = '2'
SOCK.sendall("*2*1*21##".encode())
caller.upload_door_status(id, 0)
SOCK.close()


print(caller.get_user_status(id))

disturbing_status = '0'

while True:

    door_preference = caller.door_preference(id)
    user_flag = caller.get_user_flag(id)
    door_status = caller.get_user_door_status(id)


    if disturbing_status=='0' or disturbing_status != caller.get_user_status(id):

        if user_flag==0:
            disturbing_status = '0'
            if  door_preference== 1 and door_status!= 1 :
                SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                SOCK.connect(("192.168.0.35", 20000))
                SOCK.sendall("*2*2*21##".encode())
                SOCK.close()
                caller.upload_door_status(id,1)

            elif door_preference == 0 and door_status!=0:
                SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                SOCK.connect(("192.168.0.35", 20000))
                SOCK.sendall("*2*1*21##".encode())
                SOCK.close()
                caller.upload_door_status(id, 0)

    if user_flag==1 and door_status!= 1 :
        SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCK.connect(("192.168.0.35", 20000))
        SOCK.sendall("*2*2*21##".encode())
        SOCK.close()
        time.sleep(7)
        caller.upload_door_status(id, 1)
        disturbing_status = caller.get_user_status(id)


