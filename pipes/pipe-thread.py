# anonymous pipes and threads, not processes; this version works on Windows

import os, time, threading

def child(pipeout):
    zzz = 0
    while True:
        # make parent wait
        time.sleep(zzz)
        # pipes are binary bytes
        msg = ('Spam %03d, %d\n' % (zzz, os.getpid())).encode()
        # send to parent
        os.write(pipeout, msg)
        # roll to 0 at 5
        zzz = (zzz+1) % 5

def parent(pipein):
    while True:
        # blocks until data sent
        line = os.read(pipein, 32)
        print("Parent %d got [%s] at %s" % (os.getpid(), line, time.time()))

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)