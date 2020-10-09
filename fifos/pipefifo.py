"""
named pipes; os.mkfifo is not available on Windows (without Cygwin);
there is no reason to fork here, since fifo file pipes are external
to processes--shared fds in parent/child processes are irrelevent;
"""


import os, time, sys
fifoname = '/tmp/pipefifo' # must open same name

def child():
    # OPEN FIFO PIPE FILE AS FD
    pipeout = os.open(fifoname, os.O_WRONLY)
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
    # open fifo as text file object
    pipein = open(fifoname, 'r')
    while True:
        # blocks until data sent
        line = pipein.readline()[:-1]
        print("Parent %d got [%s] at %s" % (os.getpid(), line, time.time()))


if __name__ == '__main__':
    if not os.path.exists(fifoname):
        # create a named pipe file
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        # run as parent if no args
        parent()
    else: # run as child process
        child()
    