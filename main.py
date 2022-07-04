'''
Алгоритм заключается в рекурсивном разделении массива на приблизительно равные подмассивы,
а те, в свою очередь, на другие примерно равные подмассивы. По завершению цикла рекурсии,
когда левая и правая часть рекурсии дойдёт до состояния еденичного элемента,
для вышедших частей массива вызывается функция merge, сливающая подмассивы
в один и сортируя их, после чего, если массив прошел через второй return со сливанием элементов,
рекурсия возвращается на шаг назад, и результат сливания массивов записывается в left или right в зависимости от того,
где рекурсия вернула значение, в какой из итераций рекурсивной функции. По итогу, финальной итерацией в функцию merge
будут переданы два примерно равных подмассива, примерно равных половине входящего массива, функция вернёт отсортированный
массив и рекурсивные итерации подойдут к концу
'''



def merge_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
          result.append(left[i])
          i += 1
        else:
          result.append(right[j])
          j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

array = [int(a) for a in input().split()]


if __name__ == '__main__':
    print(merge_sort(array))