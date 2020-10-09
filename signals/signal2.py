"""
set and catch alarm timeout signals in Python; time.sleep doesn't play
well with alarm (or signal in general in my Linux PC), so we call
signal.pause here to do nothing until a signal is received;
"""

import sys, signal, time

def now():
    return time.asctime()

# python signal handler
def onSignal(signum, stackframe):
    print("Got alarm", signum, "at", now())

while True:
    print("Setting at", now())
    signal.signal(signal.SIGALRM, onSignal)
    signal.alarm(5)
    signal.pause()