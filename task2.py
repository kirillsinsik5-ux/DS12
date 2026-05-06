import random
import time

def bubble_sort(arr):
    """
    Сортировка пузырьком
    Сложность: O(n²) в худшем случае
    """
    n = len(arr)
    # Копируем список, чтобы не изменять оригинал
    arr_copy = arr.copy()
    
    for i in range(n):
        # Оптимизация: флаг для проверки, были ли обмены
        swapped = False
        
        # Последние i элементов уже на месте
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                # Меняем элементы местами
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break
    
    return arr_copy

def optimized_bubble_sort(arr):
    """
    Оптимизированная сортировка пузырьком
    С учётом уже отсортированных элементов в конце
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if arr_copy[i - 1] > arr_copy[i]:
                arr_copy[i - 1], arr_copy[i] = arr_copy[i], arr_copy[i - 1]
                new_n = i
        n = new_n
    
    return arr_copy

# Создаем список из 10 000 случайных чисел
size = 10000
print(f"Генерация списка из {size} случайных чисел...")
original_list = [random.randint(1, 100000) for _ in range(size)]

# Проверяем, что списки одинаковые для честного сравнения
list_for_bubble = original_list.copy()
list_for_builtin = original_list.copy()

print("\n" + "="*50)
print("СОРТИРОВКА ПУЗЫРЬКОМ")
print("="*50)

# Замеряем время сортировки пузырьком
start_time = time.time()
bubble_sorted = bubble_sort(list_for_bubble)
bubble_time = time.time() - start_time

print(f"Время сортировки пузырьком: {bubble_time:.4f} секунд")

# Проверяем правильность сортировки
is_sorted = all(bubble_sorted[i] <= bubble_sorted[i+1] for i in range(len(bubble_sorted)-1))
print(f"Сортировка выполнена корректно: {is_sorted}")

print("\n" + "="*50)
print("ВСТРОЕННАЯ СОРТИРОВКА (Timsort)")
print("="*50)

# Замеряем время встроенной сортировки
start_time = time.time()
builtin_sorted = sorted(list_for_builtin)  # или list_for_builtin.sort()
builtin_time = time.time() - start_time

print(f"Время встроенной сортировки: {builtin_time:.4f} секунд")

print("\n" + "="*50)
print("СРАВНЕНИЕ")
print("="*50)
print(f"Пузырьковая сортировка: {bubble_time:.4f} сек")
print(f"Встроенная сортировка:   {builtin_time:.4f} сек")
print(f"Разница:                 {bubble_time/builtin_time:.1f}x медленнее")

# Демонстрация на маленьком списке
print("\n" + "="*50)
print("ДЕМОНСТРАЦИЯ РАБОТЫ НА МАЛЕНЬКОМ СПИСКЕ")
print("="*50)
small_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Исходный список: {small_list}")
sorted_small = bubble_sort(small_list)
print(f"Отсортированный: {sorted_small}")

# Тест на уже отсортированном списке
print("\n" + "="*50)
print("ТЕСТ НА ОТСОРТИРОВАННОМ СПИСКЕ")
print("="*50)
sorted_list = list(range(10000))
start_time = time.time()
bubble_sort(sorted_list)
bubble_sorted_time = time.time() - start_time
print(f"Пузырьком (уже отсортирован): {bubble_sorted_time:.4f} сек")

start_time = time.time()
sorted(sorted_list)
builtin_sorted_time = time.time() - start_time
print(f"Встроенной (уже отсортирован): {builtin_sorted_time:.4f} сек")