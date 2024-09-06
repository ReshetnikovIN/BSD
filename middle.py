grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
marks = {'Johnny': [[5, 3, 3, 5, 4], 0], 'Bilbo': [[2, 2, 2, 3], 0], 'Steve': [[4, 5, 5, 2], 0], 'Khendrik': [[4, 4, 3], 0], 'Aaron': [[5, 5, 5, 4, 5], 0]}

mark_book = {}
for dictelem in marks.keys():
    lenth = len(marks.get(dictelem)[0])
    mark = 0.0
    for i in range(lenth):
        mark = mark + marks.get(dictelem)[0][i]
    middle_mark: float = mark / lenth
    mark_book[dictelem] = middle_mark
print(mark_book)


