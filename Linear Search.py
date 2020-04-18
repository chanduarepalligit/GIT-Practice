def linearSearch(lst, key):
    lst2 = []
    flag = False
    for i in range(len(lst)):
        if key == lst[i]:
            flag = True
            lst2.append(i)
    if flag:
        print("Element found at index :", end=" ")
        for i in lst2:
            print(i, end=" ")
    else:
        print("Key is not found")


lst = [21, 12, 11, 19, 10, 11, 10]
key = 11
linearSearch(lst, key)
