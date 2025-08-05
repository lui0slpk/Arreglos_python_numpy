#Fn=F-1 + F-2
#f-1 va ser "a"
#f-2 va ser "b"
#Fn resultado final
a,b = 0,1
# a=0 b=1

for i in range(10+1):
    print(a)
    a,b = b,a+b

