d = input('Введите число: ')
d_cycle = int(d) // 2
#print('исх - ', d, d_cycle)
#k = 1
list_out = []
for i in range(1, d_cycle + 1, 1):
    for j in range(i + 1, d_cycle, 1):
#        print(i, j, (int(d) % (i +j) == 0), (int(d) % 2 == 0))
#        if (int(d) % (i +j) == 0) and (int(d) % 2 == 0):
        if (int(d) % (i + j) == 0):
             #   k = j
#                print('ining - ', i, j)
                list_out.append(i)
                list_out.append(j)

    if i != (int(d) - i):
#        print(i, int(d) - i)
        list_out.append(i)
        list_out.append(int(d) - i)
print('(',*list_out, ')')