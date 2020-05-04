

# Create your tests here.
T = int(input())
l = list()
for i in range(T):
    N,B = input().split()
    
    l.extend(input().split())
    
    l.sort()
    sum =0 
    count = 0
    while sum <= int(B) :
        sum += int(l.pop(0))
        if(sum <= int(B) ):
            count += 1
    print("Case #",(i+1),":",count)
    
    l.clear()