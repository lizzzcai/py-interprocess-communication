'''
To distinguish messages better, we can mandate a separator character in the pipe. An
end-of-line makes this easy, because we can wrap the pipe descriptor in a file object
with os.fdopen and rely on the file object’s readline method to scan up through the
next \n separator in the pipe.
'''

# same as pipe1.py, but wrap pipe input in stdio file object
# to read by line, and close unused pipe fds in both processes

import os, time

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


def parent():
    # make 2-ended pipe
    pipein, pipeout = os.pipe()
    # in child, write to pipe
    if os.fork() == 0:
        # close input side here
        os.close(pipein)
        child(pipeout)
    else:
        # in parent, listen to pipe
        # close output side here
        os.close(pipeout)
        # make text mode input file object
        pipein = os.fdopen(pipein)
        while True:
            # blocks until data sent
            line = pipein.readline()[:-1]
            print("Parent %d got [%s] at %s" % (os.getpid(), line, time.time()))


parent()