import threading
def my_task():
    print("Hello, world!")
my_thread = threading.Thread(target=my_task)
my_thread.start()