from pprint import pprint

class Product():
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        file_out = file.read()
        file.close()
        return file_out


    def add(self, *products: Product):
        file_read = open(Shop.__file_name, 'r')
        read_out = file_read.read()
        file_read.close()

        for st in range(len(products)):
            if str(products[st]) in read_out:
                print(f'Продукт {str(products[st])} уже есть в магазине')
            else:
                file_write = open(Shop.__file_name, 'a')
                writing_string = str(products[st]) + '\n'
                write_out = file_write.write(writing_string)
                file_write.close()
        return



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
