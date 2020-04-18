num = int(input("Enter Number : "))
k = len(str(num))
a = list(map(int, str(num)))
b = list(map(lambda x: x **k, a))
if sum(b) == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")