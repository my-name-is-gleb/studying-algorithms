"""Note: All examples work if the user enters valid data."""
"""Chapter 01"""
import bisect

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