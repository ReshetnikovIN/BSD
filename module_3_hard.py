def stuct_strint(elem):
    if isinstance(elem, str):
        res = len(elem)
    elif isinstance(elem, int) or isinstance(elem, float):
        res = elem
    return res


 # реформирование производльной структуры в список
def struct_elem(struct):
    # если входящая структура список
    if isinstance(struct, list):
        print('step 1', struct)
        new_stuct = []
        # перебиракм список
        for id_l in range(len(struct)):
            print('step 2', id_l, struct[id_l])
            # если в списке ещё список
            if isinstance(struct[id_l], list):
                print('step 3', struct[id_l])
                print('restucture')
                struct_elem(struct[id_l])
            else:
                # если не список, а элементы списка
                # print('step 3', id_l, struct[id_l])
                new = str(struct[id_l]) + '_'
                # new_stuct.append(new)
                # struct.append(new)
                removed = struct.pop(id_l)
                struct.insert(id_l, new)
                #struct.append(new)
                print('step 3', id_l, struct[id_l], new, struct)
        return struct
            #res = struct_elem(id_l)
    else:
        print('step 4')
        return new_stuct



#data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = [[1, 2, 3], [4, 5, 6]]
data = [[11, 22, 33], [44, 55, 66]]
data = [[11, 22, 33]]
print(struct_elem(data))


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
#print(data_structure)
