import threading
import time
exitFlag = 0
class MyThread (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter =counter
    def run(self):
        print ("Starting "+self.name )
        threadLock.acquire()
        print_time(self,threadName = self.name,delay = self.counter,counter = 5)
        print ("Exitting "+self.name)
        threadLock.release()
def print_time(self,threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" %(threadName,time.ctime(time.time())))
        counter -=1
if __name__ == "__main__":
    Bd = time.time() 
    threadLock=threading.Lock()
    thread1 =  MyThread(1,"thread1",1)
    thread2 =  MyThread(1,"thread2",2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    kt = time.time()
    print (kt-Bd)
    print("Exit thread")