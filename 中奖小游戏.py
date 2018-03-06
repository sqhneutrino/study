import random
print('抽奖了，抽奖了，按a抽奖')
while True:
        response=input()
        if response=='a':
                random.randint(1,100)
                r=random.randint(1,100)
                if r in range(1,5):
                        print('恭喜你，一等奖')
                        continue
                elif r in range (6,30):
                        print('恭喜你，二等奖')
                        continue
                elif r in range(31,100):
                        print('恭喜你，三等奖')
                        continue
        if response!='a':
                break
print('谢谢惠顾，欢迎下次再来')
       
