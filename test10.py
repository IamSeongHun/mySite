import sys

num=int(sys.stdin.readline())
def sum(a,b):
    return print(a+b)
a = []
for i in range(num):
    a.append(sys.stdin.readline().split())
#print(len(a))
#print(a)
#int_list=list(map(int,a))
for i in range(num):
    sum(int(a[i][0]),int(a[i][1]))   
    