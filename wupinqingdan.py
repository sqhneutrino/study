qingdan={'apple':42,'pineapple':2,'rope':5,'dingzi':7,'firestick':8,'shuitong':4,'basin':9}
total=0
for k,v in qingdan.items():
    print((k+':').ljust(15)+'          '+(str(v)+'个').rjust(5))
    total=total+qingdan.get(k,0)
print(('总共'+':').ljust(15)+(str(total)+'个').rjust(13))
