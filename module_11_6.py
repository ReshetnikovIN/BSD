import sys
import types
import inspect
import collections

class MyClass:
    def __init__(self):
        self.attri = "OK !"

def introspection_info(obj_name):

    class_am = 0
    list_am = 0
    dict_am = 0
    tuple_am = 0
    str_am = 0
    module_am = 0
    method_am = 0
    function_am = 0
    int_am = 0
    float_am = 0

    ClassDict = {}
    ListDict = {}
    DictDict = {}
    TupleDict = {}
    StrDict = {}
    IntDict = {}
    FloatDict = {}
    MethodDict = {}
    FunctionDict = {}
    ModuleDict = {}


    if inspect.getmodule(obj_name) == None:
        print(f'У объекта {obj_name} нет вызывающего модуля')
    else:
        print(f'Объект {obj_name} вызывется модулем {inspect.getmodule(obj_name)}')
    for name, data in inspect.getmembers(obj_name):

        if type(data) == type:
            class_am += 1
            ClassDict[name] = data
        if type(data) == list:
            list_am += 1
            ListDict[name] = data
        if type(data) == dict:
            dict_am += 1
            DictDict[name] = data
        if type(data) == tuple:
            tuple_am += 1
            TupleDict[name] = data
        if type(data) == str:
            str_am += 1
            StrDict[name] = data
        if type(data) == int:
            int_am += 1
            IntDict[name] = data
        if type(data) == float:
            float_am += 1
            FloatDict[name] = data
        if inspect.ismethod(data):
            method_am += 1
            MethodDict[name] = data
        if inspect.isfunction(data):
            function_am += 1
            FunctionDict[name] = data
        if inspect.ismodule(data):
            module_am += 1
            ModuleDict[name] = data

    if module_am > 0:
        print(f'Количество модулей - {module_am}')
        for name, data in ModuleDict.items():
            print(f'    Модуль {name}. Значение: {data}')
    if function_am > 0:
        print(f'Количество функций - {function_am}')
        for name, data in FunctionDict.items():
            # print(f'    Функция {name}. Значение: {data}')
            print(f'    Функция {name}')
    if module_am > 0:
        print(f'Количество классов - {class_am}')
        for name, data in ClassDict.items():
            print(f'    Класс {name}. Значение: {data}')
    if method_am > 0:
        print(f'Количество методов - {method_am}')
        for name, data in MethodDict.items():
            print(f'    Метод {name}. Значение: {data}')
    if tuple_am > 0:
        print(f'Количество кортежей - {tuple_am}')
        for name, data in TupleDict.items():
            print(f'    Кортеж {name}. Значение: {data}')
    if dict_am > 0:
        print(f'Количество словарей - {dict_am}')
        for name, data in DictDict.items():
            print(f'    Словарь {name}. Значение: {data}')
    if list_am > 0:
        print(f'Количество списков - {list_am}')
        for name, data in ListDict.items():
            print(f'    Список {name}. Значение: {data}')
    if str_am > 0:
        print(f'Количество строковых переменных - {str_am}')
        for name, data in StrDict.items():
            print(f'    Строковая переменная {name}. Значение: {data}')
    if int_am > 0:
        print(f'Количество переменных целых чисел - {int_am}')
        for name, data in IntDict.items():
            print(f'    Переменная целых чисел {name}. Значение: {data}')
    if float_am > 0:
        print(f'Количество переменных чисел с плавающей точкой - {float_am}')
        for name, data in FloatDict.items():
            print(f'    Переменная числа с плавающей точкой {name}. Значение: {data}')


a = 25
b = 1.23
c = "Help"
introspection_info(types)
# detect_obj(MyClass)
# detect_obj(a)
# detect_obj(b)
# detect_obj(c)
# print(dir(a))





