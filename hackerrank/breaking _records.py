scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    # Write your code here
mi = scores[0]
ma = scores[0]
c1 = 0
c2 = 0
n= len(scores)
for i in range (n):
        if scores[i]<mi:
            mi = scores[i]
            c1 += 1
        elif scores[i]>ma:
            ma = scores[i]
            c2 += 1

print ([c2,c1])
              
 
