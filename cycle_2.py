my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_amount = len(my_list)
i = 0
while i < list_amount:
    if my_list[i] >= 0:
        if my_list[i] == 0:
            i = i + 1
            continue
        print(my_list[i])
        i = i + 1

