# Пространственная сложность O(n)
# Большой плюс в том, что поиск по индесу занимает O(1).
class ArrayFIFO:
    # Задаем праматеры массива, вместимость должна быть больше чем 0
    def __init__(self, capacity=1):
        capacity = max(capacity, 1)
        self.__capacity = capacity
        self.__array = [0] * capacity
        self.__first = 0
        self.__size = 0

    # Получить значение по индексу и удлаить его из массива
    def getAndDel(self):
        res = self.get()
        self.__first = (self.__first + 1) % self.__capacity
        self.__size -= 1
        return res

    # Получить значение по индексу
    def get(self, index=0):
        if index < self.__size:
            return self.__array[(self.__first + index) % self.__capacity]
        elif index == 0:
            raise ValueError("В классе нет элементов")
        else:
            raise ValueError("Индекс вне границ")

    # Добавить новое значение
    def put(self, el):
        if self.__size == self.__capacity:
            self.__extend(2 * self.__capacity + 1)
        self.__array[self.__last()] = el
        self.__size += 1

    # Получить размер массива
    def size(self):
        return self.__size

    # Расширить вместимость массива на значение capacity
    def __extend(self, capacity):
        newArray = []
        size = self.size()
        for i in range(self.__size):
            newArray.append(self.getAndDel())
        newArray += [0] * (capacity - size)
        self.__size = size
        self.__array = newArray
        self.__first = 0
        self.__capacity = capacity

    def __last(self):
        if self.__size == 0:
            return self.__first
        else:
            return (self.__first + self.__size - 1) % self.__capacity + 1


# # Пространственная сложность O(n)
# Поиск по индесу занимает O(n)
class LinkedFIFO:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    # Получить первое значение и удалить его из массива
    def getAndDel(self):
        res = self.get()
        self.__first = self.__first.next
        self.__size -= 1
        return res

    # Получить первое значение
    def get(self):
        if self.size() != 0:
            return self.__first.val
        else:
            raise ValueError("В классе нет элементов")

    # Добавить новое значение
    def put(self, el):
        if self.size() == 0:
            self.__first = self.Node(el)
            self.__last = self.__first
        else:
            self.__last.next = self.Node(el)
            self.__last = self.__last.next
        self.__size += 1

    # Получить размер массива
    def size(self):
        return self.__size

    class Node:
        def __init__(self, el=None, next=None):
            self.val = el
            self.next = next