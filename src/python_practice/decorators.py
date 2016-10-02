from functools import wraps
def decorator(a_function):
    @wraps(a_function)
    def im_not_a_rapper():
        print 'IN YOLOLOLOOLOLOLO SCHWWAAAAG'
        a_function()
        print 'POST BRuh'

    return im_not_a_rapper



@decorator
def f(foo='Casey'):
    print foo

if __name__ == '__main__':
    f()
