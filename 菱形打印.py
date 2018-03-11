def lx(t):
        import time
        time1=time.time()
        for i in range(int(t)):
                print(' '*(int(t+2)-i),end='')
                for j in range (i):
                        print('* ',end='')
                print('*')
        for i in range(int(t-1)):
                print(' '*(i+4),end='')
                for j in range((int(t-2)-i)):
                        print('* ',end='')
                print('*')
        time2=time.time()
        print('用时:'+str(time2-time1)+'秒')
