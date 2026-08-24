"""Note: All examples work if the user enters valid data."""
"""Chapter 01"""
import bisect
import requests

def binary_search(my_list, number):
    low = 0
    high = len(my_list) - 1 # len(my_list) вернет общее кол-во элементов в списке, но индексы начинаются с нуля, 
                            # а значит что если в списке будет 3 элемента, то len(my_list) вернет 3, а по индексу 3 мы не чего не найдем
    while low <= high:
        mid = (low + high) // 2 # если значение (low + high) нечетно, то python округляет значение mid в меньшую сторону
        guess = my_list[mid] # получаем значение которое лежит в списке по предрологаемому индексу
        if guess == number:
            return mid
        elif guess > number:
            high = mid - 1
        else:
            low = mid + 1

my_list = [1, 2, 3, 4, 5]

print(binary_search(my_list, 3))
print(binary_search(my_list, 5))
print(binary_search(my_list, 6)) # вернется None.
                                 # - Но почему? ведь мы не прописали что будет если так не сего и не найдется!
                                 # просто в python есть правило: Если выполнение функции дошло до самого конца, 
                                 # но компьютер так и не встретил команду return с конкретным значением, 
                                 # Python автоматически и принудительно делает return None.


listes = [1, 10, 8, 13, 3]
print(sorted(listes))
listes.sort()
print(listes)
print(bisect.bisect_left(listes, 10))
bisect.insort(my_list, 3.5)
print(my_list)

"""Chapter 02"""

def findSmallest(arr):
    smaller = arr[0]
    smaller_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i

    return smaller_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([4, 6, 8, 1, 4, 3]))

"""Chapter 03"""

def recursionfunc(number):
    print(number)
    if number <= 1:
        return "end"
    else:
        return recursionfunc(number-1)

print(recursionfunc(int(input("> "))))

"""Chapter 04"""

def gcd(a: int, b: int) -> int:
    if b == 0: # Базовый случай: если b стало нулем, значит а — это наибольший общий делитель(НОД)
        return a
    # Рекурсивный шаг: вызываем функцию заново, 
    # передавая b и остаток от деления a на b
    return gcd(b, a % b) # знак % показывает сколько останется после деления нацело. Пример: 10/3,
                         # нацело можно поделить три раза и останется один, тоесть 10%3 - выведет 1
 
print(gcd(105, 33))  # Выведет: 3 
"""Опишем работу програмы:
   1. в функцию под аргумент а приходит число 105, под аргумент b - 33
   2. базовый случай игнорируется так-как  b == 33, а не 0
   3. функция идет дальше и происходит рекурсивный случай
   4. под аргумент а попадает 33, а под аргумент b - 6, так как 105 = 33*3+'6'
   5. запускается подфункция в стеке, и базовый случай опять игнорируется так как под аргументом b не 0, a 6
   6. запускается ещё одна подфункция под аргументом а будет 6, а под аргументом b - а%b(33%6) и будет 3, ведь 33=6*5+3
   7. базовый случай опять игнорируется так-как под аргументом b не 0, а 3
   8. запускается ещё одна подфункция под аргументом а будет 3, а под аргументом b - а%b(6%3) и будет 0, ведь 6=3*2
   9. базовый случай наконец не игнорируется ведь под аргументом b как раз 0
   10. а как на верх возвращяется 3? - как матрешка! мы ведь в под функциях пишем return gcd(b, a % b), и в итоге везде возвращяется 3!"""

# exercise 4.1
"""loop"""
def sum_numbers(sumlist: list) -> int:
    suma = 0
    for number in sumlist:
        suma += number
    return suma

"""recursion"""
index = 0
def sum_numbers(sumlist: list) -> int:
    global index
    if index == len(sumlist) - 1:
        return sumlist[index]
    suma = sumlist[index]
    index += 1
    return suma + sum_numbers(sumlist)

print(sum_numbers([11, 45, 32, 89]))

# exercise 4.2
all_element = 0
def search_all_element(findlist: list) -> int:
    global all_element
    if not findlist:
        return all_element
    del findlist[0]
    all_element += 1
    return search_all_element(findlist)

print(search_all_element([11, 3, 56]))

# exercise 4.3
"""loop"""
def search_biggest_number(findlist: list) -> int:
    biggest_number = 0
    for number in findlist:
        if number >= biggest_number:
            biggest_number = number
    return biggest_number

print(search_biggest_number([11, 3, 56]))

"""recursion"""
biggest_number = 0
def search_biggest_number(findlist: list) -> int:
    global biggest_number
    if not findlist:
        return biggest_number
    if findlist[0] >= biggest_number:
        biggest_number = findlist[0]
    del findlist[0]
    return search_biggest_number(findlist)

print(search_biggest_number([11, 3, 56]))


def Quicksort(sortlist: list) -> list:
    if sortlist:
        if len(sortlist) == 1:
            return sortlist
        mid_index = len(sortlist) // 2
        pivot = sortlist[mid_index]
        del sortlist[mid_index]
        small_sorted_list = []
        big_sorted_list = []
        for number in sortlist:
            if number >= pivot:
                big_sorted_list.append(number)
            elif number < pivot:
                small_sorted_list.append(number)
            else:
                print("Слушай ну я хуй знаю что может быть и не больше и не меньше и не равно")
        return Quicksort(small_sorted_list) + [pivot] + Quicksort(big_sorted_list)
    else:
        return []

mylist = [3, 5, 11, 4, 89, 54, 1, 2, 1, 1, 45]
print(Quicksort(mylist))

"""Chapter 05"""

from typing import Any
book = dict()
book = {} # сокращенная запись(abbreviated notation)
book["apple"] = 0.54
book["avocado"] = 1.49
book["milk"] = 2.0
print(book)
print(book["apple"])
print(book["avocado"])
print(book["milk"])
"""Поиск в словарях работает намного быстрее даже бинарного поиска! Он работает за время O(1)"""
"""Dictionary lookup is much faster than even binary search! It operates in O(1) time."""

def checking(dictionary: dict, element_under_test: Any) -> bool:
    if element_under_test in dictionary:
        return True
    else:
        return False
    
phone_book = {
    "Misha": 7_912_456_78_90,
    "Masha": 7_926_312_85_47,
    "Kostya": 7_999_123_45_67
}
print(checking(phone_book, "Gleb"))
print(checking(phone_book, 45))
print(checking(phone_book, "Misha"))

cache = {}
def get_page(url: str):
    if cache.get(url):
        return cache[url] # Возвращаем кэшированные данные(Returning cached data)
    else:
        cache[url] = requests.get(url) # Данные сначала сохраняются в хэше(для простоты будем сохранять только статус)
                                       # The data is first saved in the cache (for simplicity, we will save only the status)
        return cache[url]

"""Chapter 06"""

from collections import deque
graph = {}
graph["Gleb"] = ["Kostya"]
graph["Kostya"] = ["Andrey"]
graph["Vova"] = ["Kostya", "Andrey"]
graph["Andrey"] = ["Mango-m"]

def person_is_seller(name):
    if name[-1] == 'm':
        return True
    else:
        return False
"""глупая проверка на то заканчивается ли слово на 'm'
   (просто код из книги)"""
search_queue = deque() # создание новой очереди
search_queue += graph["Gleb"] # все соседи добовляются в очередь поиска
searched = [] # этот список используется для отслеживания уже уже проверянныйх людей
while search_queue: # пока очередь не пуста
    person = search_queue.popleft() # из очереди извлекается первый человек
    if not person in searched: # эта проверка нужна для избежания бесконечного цикла, где один узел добовляет второй, а второй узел - первый
        if person_is_seller(person): # проверяем является ли человек продовцом манго
            print(person, "is a mango seller") # да является
            break
        else:
            search_queue += graph[person] # не является; все друзья этого человека добавятся в очередь
            searched.append(person) # помечается как уже проверянный
else:
    print("Продавцов манго нет")

"""Chapter 07"""

def find_lowest_cost_node(costs): # найти узел с минимальной стоимостью
    lower_cost = float("inf") # наименьшая стоимость (переменной присваивается бесконечность)
    lower_cost_node = None # самый маленький узел
    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed: # если стоимость проверяемого узла меньше текущей минимальной (lower_cost) и узел ещё не был проверенным 
            lower_cost = cost
            lower_cost_node = node
    return lower_cost_node

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print(graph["start"].keys())
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph['b']["end"] = 5
graph["end"] = {} # у конечного узла нет соседей
"""Каждый узел имеет свой граф"""

infinity = float("inf") # так в Python обозначается бесконечность
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None
processed = [] # массив для отслеживания уже обработанных узлов
node = find_lowest_cost_node(costs) # Найти узел с наименьшей стоимостью среди необработанных
while node is not None:
    cost = costs[node] # стоимость узла в графе costs, например, для "b" это 2
    neighbors = graph[node] # соседи узла в графе "graph", например, для "b" это {"a": 3, "end": 5}
    for i in neighbors.keys(): # в i сейчас будет "a", далее "end"
        new_cost = cost + neighbors[i] # добавляем стоимость ребра к текущей стоимости пути
        if costs[i] > new_cost: # проверяем, является ли новый путь более коротким, чем старый
            costs[i] = new_cost
            parents[i] = node # обновляем родителя, чтобы после окончания работы цикла можно было восстановить самый короткий путь
    processed.append(node) # добовляем узел в козину(уже после обработки всех его соседей)
    node = find_lowest_cost_node(costs)

"""Chapter 08"""

states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"} # тип данных - множество
stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}
"ключи - названия станций, а значения - сокращенные обозначение штатов, входящих в зону охвата"
"""фигурные скобки можно использовать чтобы обозночать как словари так и множества,
   а множества можно использовать как значение в словаре(что и илюстрируется выше)"""
final_stations = set() # для обозначения множества используем функцию set() т.к. фигурные скобки по умолчанию обозночают словарь, а не множество и это может привести к ошибки
while states: # пока остались не покрытые штаты
    best_station = None # лучшая станция
    states_covered = set() # самое большое покрытие штатов
    for station, states_for_station in stations.items(): # Метод .items() в Python возвращает пару (ключ, значение) для каждого элемента словаря
        covered = states & states_for_station # пересечение множеств
        if len(covered) > len(states_covered): # если кол-во штатов которые покрывает текущая станция, больше лучшей за прошлое время
            best_station = station
            states_covered = covered
    """в каждом цикле while выбирается лучшая станция и добовляется в список лучших станций, а также удаляются штаты которые она покрывала"""
    states = states - states_covered
    final_stations.add(best_station)
print(final_stations)

"""--------------------------------------------------"""
"Множество - уникальный тип данных!"
"С множеством можно проводить различные операции"
"*В множестве не содержится дубликатов"
velo_marks = {"Giant", "Trek", "Bmw", "Seatt"}
auto_marks = {"Lada", "Bmw", "Tesla"}
print(f"Есть два множества:\n   1. {velo_marks}\n    2. {auto_marks}\n  Объедененые множества {velo_marks|auto_marks}") # | - объединение
print(f"Есть два множества:\n   1. {velo_marks}\n    2. {auto_marks}\n  Одинаковые элементы {velo_marks&auto_marks}") # & - пересечение элементов
print(f"Есть два множества:\n   1. {velo_marks}\n    2. {auto_marks}\n  Только велики {velo_marks-auto_marks}") # разность
print(f"Есть два множества:\n   1. {velo_marks}\n    2. {auto_marks}\n  Только машины {auto_marks-velo_marks}") # разность
"""--------------------------------------------------"""

"""Chapter 09"""

pass