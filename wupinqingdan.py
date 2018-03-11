qingdan={'apple':42,'pineapple':2,'rope':5,'dingzi':7,'firestick':8,'shuitong':4,'basin':9}
def tongjdj(dict):
    total=0
    for k,v in dict.items():
        print(k+'---------'+str(v))
        total=total+dict.get(k,0)#可以用，total+=v 代替
    print('总共'+str(total)+'个')
tongjdj(qingdan)
