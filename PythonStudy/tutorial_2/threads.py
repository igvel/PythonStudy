# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

import threading, Queue

queue = Queue.Queue(5)

# User thread
class AsyncTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(100):
            print 'In Background!'
            queue.put("Package")


print 'Starting Thread'
background = AsyncTask()
background.start()

print 'Main program continues'
for i in range(100):
    package = queue.get()
    print 'In Foreground!', package

background.join()
print 'Finished!'

# Use queue