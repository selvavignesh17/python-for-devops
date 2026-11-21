# Write your code here
arr = [5,4,3,2,6,10]
arr.sort()
n = len(arr)
i=0
min = 0
max = 0
answer = 0
for i in range (n-1):
    min += arr[i]
        
for i in range (1,n):
    max += arr[i]

print(str(min)+ " " + str(max))