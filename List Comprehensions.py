x = int(input())
y = int(input())
z = int(input())
n = int(input())
list1=[[i j] for i in range(x+1) for j in range(y) if True]

#list1=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((x+y)!=n)]
print (list1)