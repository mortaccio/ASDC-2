import time

# Функция для чтения данных из файла и возвращения массива записей
def read_data_from_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            record = line.strip().split(',')
            data.append(record)
    return data

# Метод сортировки пузырьком
def bubble_sort(data, key_index):
    comparisons = 0
    swaps = 0
    start_time = time.time()

    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparisons += 1
            if data[j][key_index] > data[j + 1][key_index]:
                swaps += 1
                data[j], data[j + 1] = data[j + 1], data[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return comparisons, swaps, execution_time

# Метод сортировки выбором
def selection_sort(data, key_index):
    comparisons = 0
    swaps = 0
    start_time = time.time()

    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if data[j][key_index] < data[min_index][key_index]:
                min_index = j

        swaps += 1
        data[i], data[min_index] = data[min_index], data[i]

    end_time = time.time()
    execution_time = end_time - start_time

    return comparisons, swaps, execution_time

# Метод сортировки слиянием
def merge_sort(data, key_index):
    def merge(left, right):
        merged = []
        i = j = 0
        comparisons = 0
        swaps = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i][key_index] <= right[j][key_index]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                swaps += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        swaps += len(left[i:])

        return merged, comparisons, swaps

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr, 0, 0

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left, left_comparisons, left_swaps = merge_sort_recursive(left)
        right, right_comparisons, right_swaps = merge_sort_recursive(right)

        merged, merge_comparisons, merge_swaps = merge(left, right)

        comparisons = left_comparisons + right_comparisons + merge_comparisons
        swaps = left_swaps + right_swaps + merge_swaps

        return merged, comparisons, swaps

    start_time = time.time()

    sorted_data, comparisons, swaps = merge_sort_recursive(data)

    end_time = time.time()
    execution_time = end_time - start_time

    return comparisons, swaps, execution_time


# Основная часть программы
file_name = 'data.txt' 
key_index = 1  # Индекс ключевого поля для сортировки

data = read_data_from_file(file_name)

print("Bubble Sort:")
comparisons, swaps, execution_time = bubble_sort(data.copy(), key_index)
print("Theoretical Complexity: O(n^2)")
print("Number of Comparisons:", comparisons)
print("Number of Swaps:", swaps)
print("Execution Time:", execution_time, "seconds")

print()

print("Selection Sort:")
comparisons, swaps, execution_time = selection_sort(data.copy(), key_index)
print("Theoretical Complexity: O(n^2)")
print("Number of Comparisons:", comparisons)
print("Number of Swaps:", swaps)
print("Execution Time:", execution_time, "seconds")

print()

print("Merge Sort:")
comparisons, swaps, execution_time = merge_sort(data.copy(), key_index)
print("Theoretical Complexity: O(n log n)")
print("Number of Comparisons:", comparisons)
print("Number of Swaps:", swaps)
print("Execution Time:", execution_time, "seconds")


