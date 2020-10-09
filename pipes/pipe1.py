'''
If you look closely at the preceding output, you’ll see that when the child’s delay counter
hits 004, the parent ends up reading two messages from the pipe at the same time.
'''

import os, time

def child(pipeout):
    zzz = 0
    while True:
        # make parent wait
        time.sleep(zzz)
        # pipes are binary bytes
        msg = ('Spam %03d' %zzz).encode()
        # send to parent
        os.write(pipeout, msg)
        # goto 0 after 4
        zzz = (zzz+1) % 5

def parent():
    # make 2-ended pipe
    pipein, pipeout = os.pipe()
    # copy this process
    if os.fork() == 0:
        # in copy, run child
        child(pipeout)
    else:
        # in parent, listen to pipe
        while True:
            # blocks until data sent
            line = os.read(pipein, 32)
            print("Parent %d got [%s] at %s" % (os.getpid(), line, time.time()))

parent()