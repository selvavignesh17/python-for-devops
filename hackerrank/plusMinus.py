arr = [1, 2, 3, -1, -2, -3, 0, 0]
n = len(arr)
positive_count = 0
negative_count = 0
zero_count = 0

for i in range(n):
    if arr[i] > 0:
        positive_count += 1
    elif arr[i] < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"{positive_count/n:.6f}")
print(f"{negative_count/n:.6f}")
print(f"{zero_count/n:.6f}")