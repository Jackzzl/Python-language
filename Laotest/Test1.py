"""test1
w=input('wigth: ')
wight=float(w)
h=input('height: ')
height=float(h)
test=wight/(height*height)
if test<18.5:
    print('过轻')
elif 25>test>=18.5:
    print('正长')
elif test>=25:
    print('过胖')
"""
"""test2
names=['J','K','T']
for name in names:
    print(name)
#test3
sum =0
for x in range(101):
    sum =sum +x
print(sum)

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-10))
""""""
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

"""
"""
from functools import reduce
CHAR_TO_int={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    ints = map(lambda ch:CHAR_TO_int[ch],s)
    return reduce(lambda x,y: x*10+y,ints)

print(str2int('0012345'))
"""
"""
#test1 string to float
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}
from functools import reduce
def str2float(s):
    nums=map(lambda ch: CHAR_TO_FLOAT[ch],s)
    point =0
    def to_float(f,n):
        nonlocal point
        if n==-1:
            point =1
            return f
        if point ==0:
            return f*10+n
        else:
            point = point *10
            return f+n/point
    return reduce(to_float,nums,0.0)

print(str2float('123.456'))
print(str2float('0.12324'))
"""
"""
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s %s'%(self.name,self.score))

bart= Student('Tim',50)
bart.print_score()
"""

"""
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_core(self):
        print('%s:%s' % (self.name, self.age))


stu1 = Student('tpc', 26)
stu1.print_core()
#############
import time, threading

def loop():
    print('thread %s is running ...'%threading.current_thread().name)
    n=0
    while n <5:
        n+=1;
        print('thread %s >>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.'% threading.current_thread().name)

print('thread %s is running ...'% threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended'% threading.current_thread().name)"""
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')