def set_unwrap(data_in):
    global result
    for ele in data_in:
        if isinstance(ele, list):
            set_res = list_unwrap(ele)
        elif isinstance(ele, tuple):
            set_res = list(tupl_unwrap(ele))
        elif isinstance(ele, dict):
            set_res.append(dict_unwrap(ele))
        else:
            set_res.append(ele)
            result.append(ele)
    return set_res


def list_unwrap(data_in):
    for ele in data_in:
        if isinstance(ele, list):
            after_list = list_unwrap(ele)
        elif isinstance(ele, tuple):
            if ele != ():
                list_res.append(list(tupl_unwrap(ele)))
        elif isinstance(ele, dict):
            list_res.append(dict_unwrap(ele))
        elif isinstance(ele, set):
            list_res.append(set_unwrap(ele))
        else:
            result.append(ele)
            list_res.append(ele)
    return list_res


def tupl_unwrap(data_in):
    global tupl_res
    for ele in data_in:
        if isinstance(ele, tuple):
            if ele != ():
                if (isinstance(ele, str) or isinstance(ele, int)):
                    tupl_res = tupl_res + ele
                    result.append(list(ele))
                else:
                    tupl_unwrap(ele)
        elif isinstance(ele, list):
            tupl_res = tupl_res + (list_unwrap(ele),)
        elif isinstance(ele, dict):
            tupl_res = tupl_res + (dict_unwrap(ele),)
        elif isinstance(ele, set):
            tupl_res = tupl_res + (set_unwrap(ele),)
        else:
            result.append(ele)
            tupl_res = tupl_res + (ele,)
    return tupl_res


def dict_unwrap(data_in):
    global result
    dict_res = []
    for key1, value1 in data_in.items():
        if isinstance(key1, str) or isinstance(key1, int):
            dict_res.append(key1,)
            dict_res.append(value1,)
            result.append(key1)
            result.append(value1)
        else:
            if isinstance(key1, list):
                dict_res.append(list_unwrap(key1))
                result.append(key1)
            elif isinstance((key1, tuple)):
                dict_res.append(list(tupl_unwrap(key1)))
                result.append(key1)
            elif isinstance((key1, set)):
                dict_res.append(set_unwrap(key1))
                result.append(key1)
            if isinstance(value1, list):
                dict_res.append(list_unwrap(value1))
            elif isinstance((value1, tuple)):
                dict_res.append(list(tupl_unwrap(value1)))
            elif isinstance((value1, set)):
                dict_res.append(set_unwrap(value1))
    return dict_res


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
list_res = []
result = []
tupl_res = ()
dict_res = ()

def calculate_structure_sum(data_structure):
    data_in =  data_structure
    if isinstance(data_in, list):
        list_unwrap(data_in)
    elif isinstance(data_in, tuple):
        tupl_unwrap(data_in)
    elif isinstance(data_in, dict):
        dict_unwrap(data_in)

    sum = 0
    for id in result:

        if isinstance(id, str):
            m = len(id)
            sum += m
        elif isinstance(id, int):
            sum += id
    return sum

result = calculate_structure_sum(data_structure)
print(result)