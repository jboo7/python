import socket,threading


def f():
    for i in range(10):
        print i,
    print

t = threading.Thread()
t.run = f
t.start()
t.join()


'''
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ss.bind(('localhost', 2323))
ss.listen(0)
while True:
    s, addr = ss.accept()
    s.send('1234567890')
    s.close()
    print addr
    break

ss.close()
'''