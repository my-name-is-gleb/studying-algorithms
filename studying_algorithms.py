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