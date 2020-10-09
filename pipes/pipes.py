"""
spawn a child process/program, connect my stdin/stdout to child process's
stdout/stdin--my reads and writes map to output and input streams of the
spawned program; much like tying together streams with subprocess module;


os.fork
    Copies the calling process as usual and returns the child’s process ID in the parent
    process only.
os.execvp
    Overlays a new program in the calling process; it’s just like the os.execlp used
    earlier but takes a tuple or list of command-line argument strings (collected with
    the *args form in the function header).
os.pipe
    Returns a tuple of file descriptors representing the input and output ends of a pipe,
    as in earlier examples.
os.close(fd)
    Closes the descriptor-based file fd.
os.dup2(fd1,fd2)
    Copies all system information associated with the file named by the file descriptor
    fd1 to the file named by fd2.
    In terms of connecting standard streams,

"""
import os, sys

def spawn(prog, *args): # pass program, cmdline args
    # get descriptors for streams
    # normally stdin=0, stdout=1
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()

    # make two IPC pipe channels, pipe returns (inputfd, outputfd)
    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout = os.pipe()
    # make a copy if this process
    pid = os.fork()
    if pid: # in parent process after fork:
        # close child ends in parent
        os.close(childStdout)
        os.close(childStdin)
        # my sys.stdin copy = pipe1[0]
        os.dup2(parentStdin, stdinFd)
        # my sys.stdout copy = pipe2[1]
        os.dup2(parentStdout, stdoutFd)
    else: # in child process         
        # close parent ends in child
        os.close(parentStdin)
        os.close(parentStdout)
        # my sys.stdin copy = pipe2[0]
        os.dup2(childStdin, stdinFd)
        # my sys.stdout copy = pipe1[1]
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        # new program in this process
        os.execvp(prog, args)
        # os.exec call never return here
        assert False, 'execvp failed!'


if __name__ == '__main__':
    mypid = os.getpid()
    # fork child program
    spawn('python', 'pipes-testchild.py', 'spam')
    # to child's stdin
    print('Hello 1 from parent', mypid)
    # subvert stdio buffering
    sys.stdout.flush() 
    # from child's stdout
    reply = input() 
    # stderr not tied to pipe!
    sys.stderr.write('Parent got: "%s"\n' % reply) 
    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])