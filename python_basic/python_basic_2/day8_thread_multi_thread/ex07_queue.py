import queue
import threading
import time

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        process_data(self.name, self.q)
        print("Exiting " + self.name)


def process_data(threadName, q):
    global exitFlag
    while not exitFlag:
        # Get lock to synchronize threads
        queueLock.acquire()
        if not q.empty():
            time.sleep(1)
            data = q.get()
            # Free lock to release next thread
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            # Free lock to release next thread
            queueLock.release()
            time.sleep(1)
            exitFlag = 1


if __name__ == "__main__":
    # danh sách tên thread
    threadList = ["Thread-1", "Thread-2", "Thread-3"]

    # d? li?u g?c
    nameList = ["Zero", "One", "Two", "Three", "Four",
                "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    queueLock = threading.Lock()

    # d? li?u hàng d?i dành cho các thread x? lý d?c,
    # b?o d?m m?t th?i di?m ch? có m?t thread chi?m gi?
    workQueue = queue.Queue()

    # danh sách thread
    threads = []
    
    # id các thread b?t d?u t? 1
    threadID = 1

    # Fill the queue
    for word in nameList:
        workQueue.put(word)

    # Create new threads
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Continue main thread
    print("Exiting Main Thread")