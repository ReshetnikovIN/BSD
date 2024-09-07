numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
Lenth_ = len(numbers)
for i in range(1, Lenth_, 1):
    print(numbers[i])
    flag_of_simple = 0
    for j in range(1, Lenth_, 1):
        print(numbers[i], numbers[j], numbers[i] % numbers[j])
        if numbers[i] % numbers[j] == 0:
            flag_of_simple = flag_of_simple + 1
    if flag_of_simple == 1:
        primes.append(numbers[i])
    if flag_of_simple >= 2:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)


