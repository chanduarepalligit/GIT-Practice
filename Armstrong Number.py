num = 153
k = len(str(num))
a = list(map(int, str(num)))
b = list(map(lambda x: x ** k, a))
if sum(b) == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

num = 153
k = len(str(num))
res = 0
i = num
while i > 0:
    temp = i % 10
    res = res + temp ** k
    i = i // 10
if res == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
