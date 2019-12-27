import time, functools
# 装饰器deractor
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start = datetime.datetime.now
#         print(start)
#         # end = datetime.datetime.now
#         # print(end)
#         print('%s executed in %s ms' % (fn.__name__, start))
#         return fn
#     return wrapper
# return metric

# @metric
# def printtime():
#     print(datetime.datetime.now())
#打印函数执行时间
def log(text=''):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t_begin = time.time()
            print('%s start at %0.4f' % (fn.__name__, t_begin))
            res = fn(*args, **kwargs)
            print(res)
            t_end = time.time()
            print('%s end at %0.4f' % (fn.__name__, t_end))
            print('%s%s executed in %s ms' % (text, fn.__name__, t_end - t_begin))
            return res
        return wrapper
    return metric
 
 
@log()
def fast(x, y):
    time.sleep(0.0012)
    return x + y
 
 
@log()
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z
 
if __name__ == "__main__":
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')   
  


