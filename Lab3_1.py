'''
Вправа 1

Визначити кількість трицифрових чисел, сума цифр яких дорівнює
деякому цілому значенню n, яке вводить користувач.
Токар Іван
'''
n = int(input("Enter a number: "))
count = 0
for i in range(100, 1000):
    if sum(int(digit) for digit in str(i)) == n:
        count += 1
print(count)