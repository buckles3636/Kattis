temp_count = input()
temps = input().split()
count = 0
for i in range(len(temps)):
    if int(temps[i]) < 0:
        count += 1
    else:
        pass
print(count)