def is_prime(func):
    def primus (*args):
        k = 0
        data_in = func(*args)
        for i in range(2, data_in // 2 + 1):
            if (data_in % i == 0):
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
        return data_in
    return primus

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)