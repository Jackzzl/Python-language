"""
import sys
sys.stdout.write('welcome to China')
import sys
print ("wlcome")
import sys
#sys.stdout=open('data/temp.txt','a')
print("welcome")
"""
"""
#sys.stdout.close()
#sys.stdout=previous
i=0
while i<5:
    i+=1
    print(i),
else :
    print(0),
"""
"""
i=0
while True:
    if i>4:
        break
    i+=1
    print(i)
"""
"""
i=0
while i<10:
    i+=1
    if i>6:
        print(i),
    else:
        continue
for i in [1,2,3,4,5,6]:
    print (i*2),
"""
"""
for item in {'Jone':'male','claire':'female'}.values():
    #item()
    #values()
    print(item),
"""
"""
for i in range(5):
    print(i);
for i in enumerate(range(5,10)):
    print(i),
"""
"""
x=[3,4,6,7,10]
y=[1,2,3,4,5]
for x,y in zip(x,y):
    print(x,y," "),#换行空格
"""
"""
for x in range(1, 11):
  print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
  """
"""
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
"""
"""
#输出:
x='china'
if x=='us':
    print (1)
elif x== 'india':
    print (2)
elif x== 'china':
    print (3)
else :
    print (4)
"""
"""

另 外 一 种 方 法
[F,T][bool(condition)]

x=[1,0][bool(1==1)]
print (x)

"""