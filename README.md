# Python InterProcess Communication

python implementation of interprocess communication

## What is Inter Process Communication

Inter process communication (IPC) is used for exchanging data between multiple threads in one or more processes or programs. The Processes may be running on single or multiple computers connected by a network. The full form of IPC is Inter-process communication.

It is a set of programming interface which allow a programmer to coordinate activities among various program processes which can run concurrently in an operating system. This allows a specific program to handle many user requests at the same time.

Since every single user request may result in multiple processes running in the operating system, the process may require to communicate with each other. Each IPC protocol approach has its own advantage and limitation, so it is not unusual for a single program to use all of the IPC methods.

## Approaches for Inter-Process Communication

* Pipes (Anonymous pipes)
* FIFOs (Named pipes): not available in python
* Message queue
* Semaphore
* Signals
* Shared memory
* Sockets

## Why IPC

Here, are the reasons for using the interprocess communication protocol for information sharing:

* It helps to speedup modularity
* Computational
* Privilege separation
* Convenience
* Helps operating system to communicate with each other and synchronize their actions.
