import socket
import subprocess


class VLC:
    def __init__(self):
        self.SCREEN_NAME = 'vlc'

        ################################### client connection
        self.HOST = '0.0.0.0'  # 192.168.0.62localhost #192.168.0.58-mine  172.22.53.87-andrea
        self.PORT = 8081  # 8888 5000

        ################################### VLC connection
        self.VLC_HOST = 'localhost'
        self.VLC_PORT = 80
        ###################################

        cmd = subprocess.run(
            ['screen', '-ls', self.SCREEN_NAME, ],
            stdout=subprocess.DEVNULL)
        if cmd.returncode:
            subprocess.run([
                'screen',
                '-dmS',
                self.SCREEN_NAME,
                'vlc',
                '-I',
                'rc',
                '--rc-host',
                '%s:%s' % (self.VLC_HOST, self.VLC_PORT)
            ])

        ########################################################server socket
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCK.bind((self.HOST, self.PORT))
        self.SOCK.listen(1)
        self.conn, self.addr = self.SOCK.accept()
        print("Connection from: " + str(self.addr))
        # data = conn.recv(1024).decode()

        ########################################################
        self.VLC_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.VLC_SOCK.connect((self.VLC_HOST, self.VLC_PORT))

    def x(self, cmd):
        # Prepare a command and send it to VLC
        if not cmd.endswith('\n'):
            cmd = cmd + '\n'
        cmd = cmd.encode()
        '''check this one, where does it send it?'''
        self.VLC_SOCK.sendall(cmd)

    def pause(self):
        self.x('pause')

    def play(self):
        self.x('play')

    def stop(self):
        self.x('stop')

    def prev(self):
        self.x('prev')

    def next(self):
        self.x('next')

    def add(self, path):
        self.x('add %s' % (path,))

    def enqueue(self, path):
        self.x('enqueue %s' % (path,))

    def clear(self):
        self.x('clear')

    def shutdown(self):
        self.x('shutdown')

    ###########################################################
    def volup(self, steps=1):
        """Increase the volume"""
        self.x("volup {0}".format(steps))  # return; _send_command

    def voldown(self, steps=1):
        """Decrease the volume"""
        self.x("voldown {0}".format(steps))
    ###########################################################