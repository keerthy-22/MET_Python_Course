from threading import Thread
import time
class SingleThread(Thread):
    def task1(self):
        print("Preparing Tea using Single Threading...")
        print("Task1:Boil milk and tea powder")
        time.sleep(5)
        print("Task1 completed sucessfully")
    def task2(self):
        print("Tas2:Add sugar and boil")
        time.sleep(5)
        print("Task2 completed sucessfully")
    def task3(self):
        print("Task3:Filter and serve Tea")
        time.sleep(2)
        print("Tea is ready")
    def run(self):
        self.task1()
        self.task2()
        self.task3()
t1=SingleThread()
t1.start()
