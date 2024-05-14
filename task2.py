def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return iterations, arr[mid]

    if high < 0:
        return iterations, None
    else:
        return iterations, arr[low] if low < len(arr) else None

# Приклад використання:
sorted_array = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
target = 1.6

iterations, upper_bound = binary_search(sorted_array, target)
print("Кількість ітерацій:", iterations)
if upper_bound is not None:
    print("Верхня межа:", upper_bound)
else:
    print("Елемент не знайдено або межа не визначена")