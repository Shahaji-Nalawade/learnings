import datetime
def decorator_func(func):
    
    print("function start time", datetime.datetime.now())
    func()
    print("fucntion end time", datetime.datetime.now())

