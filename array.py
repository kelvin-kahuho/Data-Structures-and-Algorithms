new_list = [1, 2, 3, 4, 5]
element = new_list[0]
print(element)

if 1 in new_list:
    print(True)
else:
    print(False)


for n in new_list:
    if n == 1:
        print(True)
        break
    else:
        print(False)

number = [12, 13, 14, 15, 16, 17, 18, 19, 20]
number.extend([17, 18, 19, 20, 21, 22, 23, 24])
print(number)
