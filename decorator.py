from functools import wraps

def Time(num):
    def do_multi_times(func):
        def wrapper():
            for i in range(num):
                func()
        return wrapper
    return do_multi_times



@Time(3)
def print_hello():
    print("hello")

print_hello()



