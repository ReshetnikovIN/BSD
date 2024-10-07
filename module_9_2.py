first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(st) for st in first_strings if len(st) > 5 ]

second_result = [(st_1,) + (st_2,) for st_1 in first_strings for st_2 in second_strings if len(st_1) == len(st_2)]

third_result  = [{st: len(st)} for st in (first_strings + second_strings) if not len(st) % 2 ]

print(first_result)
print(second_result)
print(third_result)
