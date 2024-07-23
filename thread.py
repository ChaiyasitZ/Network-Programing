from threading import Thread

class myThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        print("Hello, my name is %s\n" % self.name)

# Create thread instances
process1 = myThread("Thread-1")
process2 = myThread("Thread-2")
process3 = myThread("Thread-3")

# Start the threads
process1.start()
process2.start()
process3.start()