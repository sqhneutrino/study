#!pythonPython 3.6.4 
def collatz(num):
    if int(num) % 2==0:
	    return int(num)//2#可以这么写，只返回一个数也行
    if int(num) % 2==1:
	    return int (num)*3+1
import time
print('请输入数字：')
r = input()#这里不加int函数也行，因为collatz函数会把它整数化
time1 = time.time()#该函数输出的是数值
while True:
    collatz(r)
    if collatz(r)!=1:
        print(collatz(r))
        r=collatz(r)#这里的重复赋值要记得，不然r值不会变
        continue
    else:
        print(collatz(r))
        break
time2 = time.time()
print('计算完毕，本次用时:'+str(round((time2-time1),6))+'秒')#round（number，digits）函数,number为要四舍五入的数，
                                                       #digits为保留的位数

