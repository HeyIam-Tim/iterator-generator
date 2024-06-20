# refrigerator = ["bread", "milk", "apple", "meat"]

# for obj in refrigerator:
#     print(obj)
#
# print(iter(refrigerator))

# получаем итератор для итерируемого объекта
# it = iter(refrigerator)
#
# try:
#     while True:
#         next_val = next(it)
#         print("Очередное значение:", next_val)
# except StopIteration:
#     # явно напечатаем сообщение об окончании итерации,
#     # хотя цикл for этого не делает и ошибка просто подавляется
#     print("Итерация закончена")
# print("Программа завершена")


class RefrigeratorIterator:
    def __init__(self, some_objects):
        print(some_objects)
        self.some_objects = some_objects
        self.current = 0
        self.objects_length = len(self.some_objects)

    def to_start(self):
        self.current = 0

    def to_current(self, val):
        if val >= len(self.some_objects) or val < 0:
            print("Неверное значение для курсора!")
        else:
            self.current = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.objects_length:
            result = self.some_objects[self.current]
            if result == 'meat':
                self.to_current(self.current + 2)
            else:
                self.current += 1
            return result
        raise StopIteration


class Refrigerator:
    """Холодильник"""

    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def add_to_box(self, obj, box_num):
        if box_num not in self.boxes:
            print("Вы ввели неправильный номер ящика!")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in self.boxes:
            print("Вы ввели неправильный номер ящика!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)

    # def __iter__(self):
    #     # получаем сумму предметов всех ящиков
    #     boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
    #     # получаем итератор от списка и возвращаем его
    #     it = iter(boxes_items)
    #     return it

    def __iter__(self):
        return RefrigeratorIterator(self.boxes[1] + self.boxes[2] + self.boxes[3])


refrigerator = Refrigerator()
refrigerator.add_to_box("bread", 1)
refrigerator.add_to_box("milk", 2)
refrigerator.add_to_box("apple", 3)
refrigerator.add_to_box("meat", 1)


# print(refrigerator)


# my_shiny_list = [
#     ["Это", "список", "внутри", "списка"],
#     {"Это", "множество", "внутри", "списка"},
#     "Это строка внутри списка",
#     refrigerator,
# ]

# for some_collection in my_shiny_list:
#     for el in some_collection:
#         print(el)


# print(iter(refrigerator))


# it = iter(refrigerator)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for item in refrigerator:
#     print(item)

def func_l(n):
    item_list = []
    cnt = 0
    while cnt < n:
        item_list.append(cnt)
        cnt += 1
    return item_list


def func2():
    print('пришли')
    yield 1
    print('дай еще')
    yield 1
    print('ушли')


# print(dir(func2()))
# print(func2())
# print(func2)

# g = func2()
# print(next(g))
# print('Middle')
# print(next(g))
# print(next(g))


def func_wg(n):
    counter = 0
    while counter < n:
        yield counter
        counter += 1


# wg = func_wg(10)
# print(next(wg))
# print(next(wg))
# print(next(wg))

import time
import sys

start = time.time()
print('START: ', start)

l = func_l(100_000_000)
# g = func_wg(100_000_000)

# try:
#     while True:
#         next(g)
# except:
#     print('DONE')

# for item in g:
#     item
#
#
# for item in l:
#     item

print('SIZE: ', sys.getsizeof(l))
print('FINISH: ', time.time() - start)

# print(True if 10_00_0 == 10000 else False)