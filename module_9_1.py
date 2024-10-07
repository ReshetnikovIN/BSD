def apply_all_func(int_list, *functions):
    fun_res = {}
    int_list_ = []
    int_list_.append(int_list)
    for fun in functions:
        map_res = map(fun, int_list_)
        list_map_res = list(map_res)[0]
        fun_res[fun.__name__] = list_map_res
    return fun_res


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

