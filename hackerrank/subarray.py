s =[1, 2, 1, 3, 2]
count = 0 
n = len(s)
m=2
d=3
    
for i in range (n - m+1):
    segment = sum(s[i:m+i])
    if(segment == d):
            count += 1
    
print(count)