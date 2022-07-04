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