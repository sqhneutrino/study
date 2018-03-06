#！python 3
#猜数字，与书56页做对比，比书上多调用了一个函数，尽量避免这种情况。
print('请输入你的数字，100以内：')
import random
import sys
random.randint(1,20)#这个可以不用写，直接写下面一行
r = random.randint(1,100)
for i in range(10):
        k = input()
        if int(k) < int(r):
                print('小了')
                #continue
        elif int(k) > int(r):
                print('大了')
                #continue(可加可不加)
        elif int(k) == int(r):
                print('恭喜你猜对了，这个数字是:'+ str(r))
                sys.exit()
print('很可惜，次数已用完。这个数字是：'+str(r))
