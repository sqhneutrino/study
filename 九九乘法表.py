#!python3
for i in range(1,10):
	for j in range (1,i+1):
		if i!=j:
			print(str(j)+'×'+str(i)+'='+str(j*i),end='  ')
		if i==j:
			print(str(j)+'×'+str(i)+'='+str(j*i))
