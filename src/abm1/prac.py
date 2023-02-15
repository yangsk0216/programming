import random
import math
#随机坐标
list0=[random.randint(1, 100) for i in range(2)]
list1=[random.randint(1, 100) for i in range(2)]

print("list0",list0,"list1",list1)
#计算两点之间距离
distance=math.sqrt((list0[0]-list1[0])**2+(list0[1]-list1[1])**2)
print("distance",distance)

r=random.random()
if r>0.5:
    list0[0]= list0[0]+1
else:
    list0[0]-=1  
r=random.random()
if r>0.5:
    list0[1]= list0[1]+1
else:
    list0[1]-=1 
r=random.random()
if r>0.5:
    list1[0]=  list1[0]+1
else:
    list1[0]-=1  
r=random.random()
if r>0.5:
    list1[1]=list1[1]+1
else:
    list1[1]-=1 
    
    
    
    
print(list0,list1)
distance=math.sqrt((list0[0]-list1[0])**2+(list0[1]-list1[1])**2)
print("distance",distance)
    
    