import os, time, sys

mypid = os.getpid()
parentpid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' % (mypid, parentpid, sys.argv[1]))


for i in range(2):
    # make parent process wait by sleeping here
    time.sleep(3) 
    # stdin tied to pipe: comes from parent's stdout
    recv = input() 
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, recv)
    # stdout tied to pipe: goes to parent's stdin
    print(send) 
    #  make sure it's sent now or else process blocks
    sys.stdout.flush()