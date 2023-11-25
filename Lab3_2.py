prev_num = int(input("Enter a number: "))
count = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    if num > prev_num:
        count += 1
    prev_num = num
print(count)