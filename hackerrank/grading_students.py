grades = [73,45,84,89,30]
n = len(grades)
for i in range (n):
    if((grades[i]+1) % 5 == 0 and grades[i] >= 38):
            grades[i] = grades[i] + 1
    elif ((grades[i]+2) % 5 == 0 and grades[i] >= 38 ):
            grades[i] = grades[i] + 2
            
print(grades)