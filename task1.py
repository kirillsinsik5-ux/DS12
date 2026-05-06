import random
import time
import bisect

def linear_search(arr, target):
    """Линейный поиск элемента в списке"""
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

def binary_search(arr, target):
    """Бинарный поиск элемента в отсортированном списке"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    # 1. Создаем список из 1 000 000 случайных чисел
    print("Создание списка из 1 000 000 случайных чисел...")
    random_list = [random.randint(1, 1000000) for _ in range(1_000_000)]
    print(f"Список создан. Первые 10 элементов: {random_list[:10]}")
    
    # Выбираем случайное число для поиска (из середины списка)
    target = random_list[500_000]
    print(f"\nИщем число: {target}")
    
    # 2. Линейный поиск
    print("\n--- Линейный поиск ---")
    start_time = time.time()
    linear_index = linear_search(random_list, target)
    linear_time = time.time() - start_time
    
    if linear_index != -1:
        print(f"Элемент найден на позиции: {linear_index}")
    else:
        print("Элемент не найден")
    print(f"Время выполнения: {linear_time:.6f} секунд")
    
    # 3. Сортировка списка
    print("\n--- Сортировка списка ---")
    start_time = time.time()
    sorted_list = sorted(random_list)  # Создаем отсортированную копию
    sort_time = time.time() - start_time
    print(f"Время сортировки: {sort_time:.6f} секунд")
    
    # 4. Бинарный поиск
    print("\n--- Бинарный поиск ---")
    start_time = time.time()
    binary_index = binary_search(sorted_list, target)
    binary_time = time.time() - start_time
    
    if binary_index != -1:
        print(f"Элемент найден на позиции: {binary_index}")
    else:
        print("Элемент не найден")
    print(f"Время выполнения: {binary_time:.6f} секунд")
    
    # 5. Сравнение времени
    print("\n" + "="*50)
    print("СРАВНЕНИЕ ВРЕМЕНИ ВЫПОЛНЕНИЯ:")
    print(f"Линейный поиск:    {linear_time:.6f} сек")
    print(f"Бинарный поиск:    {binary_time:.6f} сек (+ сортировка {sort_time:.6f} сек)")
    print(f"Бинарный поиск (только поиск): {binary_time:.6f} сек")
    print(f"Линейный быстрее в: {binary_time/linear_time:.2f} раза" if binary_time > linear_time else f"Бинарный быстрее в: {linear_time/binary_time:.2f} раза")
    
    print(f"\nВремя сортировки составляет: {sort_time/linear_time*100:.1f}% от времени линейного поиска")
    print(f"Время бинарного поиска составляет: {binary_time/linear_time*100:.1f}% от времени линейного поиска")
    
    # Дополнительный тест: бинарный поиск с помощью встроенной функции bisect
    print("\n--- Бинарный поиск (bisect) ---")
    start_time = time.time()
    bisect_index = bisect.bisect_left(sorted_list, target)
    if bisect_index < len(sorted_list) and sorted_list[bisect_index] == target:
        bisect_time = time.time() - start_time
        print(f"Элемент найден на позиции: {bisect_index}")
        print(f"Время выполнения: {bisect_time:.6f} секунд")

if __name__ == "__main__":
    main()