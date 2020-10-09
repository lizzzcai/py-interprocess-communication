"""
catch signals in Python; pass signal number N as a command-line arg,
use a "kill -N pid" shell command to send this process a signal; most
signal handlers restored by Python after caught (see network scripting
chapter for SIGCHLD details); on Windows, signal module is available,
but it defines only a few signal types there, and os.kill is missing;
"""

import sys, signal, time

def now():
    # current time string
    return time.ctime(time.time())

def onSignal(signum, stackframe):
    # python signal handler
    # most handlers stay in effect
    print("Got signal", signum, "at", now())

signum = int(sys.argv[1])
# install signal handler
signal.signal(signum, onSignal)
while True:
    # wait for signals (or: pass)
    signal.pause()
