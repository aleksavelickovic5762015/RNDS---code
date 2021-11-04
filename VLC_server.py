from VLC_class import VLC

vlc = VLC()

vlc.add('C:\\Users\\gioia\\Desktop\\DCIM\\video-1511460309.mp4') #/home/leka/Music/Nirvana-Where-Did-You-Sleep-Last-Night-Lyrics.mp3 /Users/andrea/Desktop/Misure_lez_30.mp4 DjordjeBalasevic-Ringispil-(Audio 1991)HD.mp3
while True:
    command = vlc.conn.recv(1024).decode()
    if not command:
        break
    print("from connected  user: " + str(command))
    vlc.x(command)

print("it went out of server's while loop")