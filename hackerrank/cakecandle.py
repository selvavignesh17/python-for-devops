candles = [1, 2, 2, 1, 3]
n = len(candles)
count = 0
temp = 0
for i in range(n):
    if candles[i] >= temp:
        temp = candles[i]

for i in range(n):
    if candles[i] == temp:
        count += 1

print(count)