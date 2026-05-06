import random
import time
from typing import List, Tuple, Optional

class Student:
    """Класс, представляющий студента"""
    def __init__(self, name: str, group: str, grade: float):
        self.name = name
        self.group = group
        self.grade = grade
    
    def __repr__(self):
        return f"Student('{self.name}', '{self.group}', {self.grade})"
    
    def __str__(self):
        return f"{self.name:20} | {self.group:10} | {self.grade:.2f}"

class StudentSearchSystem:
    """Система поиска студентов"""
    
    def __init__(self, students: List[Student]):
        self.students = students
        # Для бинарного поиска создаём отсортированную копию по баллам
        self.students_by_grade = sorted(students, key=lambda s: s.grade)
    
    def linear_search_by_name(self, name: str) -> List[Student]:
        """
        Линейный поиск по имени
        Сложность: O(n)
        """
        results = []
        for student in self.students:
            if student.name.lower() == name.lower():
                results.append(student)
        return results
    
    def binary_search_by_grade(self, target_grade: float) -> List[Student]:
        """
        Бинарный поиск по среднему баллу
        Сложность: O(log n)
        Возвращает ВСЕХ студентов с заданным баллом
        """
        # Бинарный поиск для нахождения первого вхождения
        left = 0
        right = len(self.students_by_grade) - 1
        first_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            if self.students_by_grade[mid].grade == target_grade:
                first_index = mid
                right = mid - 1  # Ищем самое левое вхождение
            elif self.students_by_grade[mid].grade < target_grade:
                left = mid + 1
            else:
                right = mid - 1
        
        # Если не нашли, возвращаем пустой список
        if first_index == -1:
            return []
        
        # Собираем все вхождения (так как баллы могут повторяться)
        results = []
        index = first_index
        while index < len(self.students_by_grade) and self.students_by_grade[index].grade == target_grade:
            results.append(self.students_by_grade[index])
            index += 1
        
        return results
    
    def search_by_grade_linear(self, target_grade: float) -> List[Student]:
        """
        Линейный поиск по баллу (для сравнения производительности)
        """
        return [s for s in self.students if s.grade == target_grade]

def generate_students(count: int) -> List[Student]:
    """Генерация случайных студентов"""
    first_names = ['Иван', 'Мария', 'Алексей', 'Елена', 'Дмитрий', 'Анна', 
                   'Сергей', 'Татьяна', 'Андрей', 'Ольга', 'Павел', 'Наталья',
                   'Михаил', 'Екатерина', 'Владимир', 'Ирина', 'Николай', 'Светлана']
    
    last_names = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов', 'Попов',
                  'Васильев', 'Соколов', 'Михайлов', 'Новиков', 'Федоров', 'Морозов']
    
    groups = ['ИС-1', 'ИС-2', 'ПИ-1', 'ПИ-2', 'ВТ-1', 'ВТ-2', 'ММ-1', 'ММ-2']
    
    students = []
    for i in range(count):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        group = random.choice(groups)
        grade = round(random.uniform(60, 100), 2)  # Баллы от 60 до 100
        students.append(Student(name, group, grade))
    
    return students

def demo_search_system():
    """Демонстрация работы системы поиска"""
    
    # Генерируем список студентов
    student_count = 10000
    print(f"Генерация {student_count} студентов...")
    students = generate_students(student_count)
    
    # Создаём систему поиска
    search_system = StudentSearchSystem(students)
    
    # Выбираем случайного студента для поиска
    random_student = random.choice(students)
    search_name = random_student.name
    search_grade = random_student.grade
    
    print("\n" + "="*70)
    print("ПОИСК ПО ИМЕНИ (ЛИНЕЙНЫЙ)")
    print("="*70)
    print(f"Ищем студента: '{search_name}'")
    
    # Линейный поиск по имени
    start_time = time.time()
    name_results = search_system.linear_search_by_name(search_name)
    linear_time = time.time() - start_time
    
    print(f"Результатов найдено: {len(name_results)}")
    print(f"Время выполнения: {linear_time:.6f} секунд")
    if name_results:
        print(f"\nНайденные студенты:")
        for student in name_results[:5]:  # Показываем первых 5
            print(f"  {student}")
        if len(name_results) > 5:
            print(f"  ... и ещё {len(name_results) - 5}")
    
    print("\n" + "="*70)
    print("ПОИСК ПО СРЕДНЕМУ БАЛЛУ (БИНАРНЫЙ)")
    print("="*70)
    print(f"Ищем студентов с баллом: {search_grade}")
    
    # Бинарный поиск по баллу
    start_time = time.time()
    grade_results_binary = search_system.binary_search_by_grade(search_grade)
    binary_time = time.time() - start_time
    
    print(f"Результатов найдено: {len(grade_results_binary)}")
    print(f"Время выполнения: {binary_time:.6f} секунд")
    if grade_results_binary:
        print(f"\nНайденные студенты:")
        for student in grade_results_binary[:5]:
            print(f"  {student}")
        if len(grade_results_binary) > 5:
            print(f"  ... и ещё {len(grade_results_binary) - 5}")
    
    print("\n" + "="*70)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ПОИСКА ПО БАЛЛУ")
    print("="*70)
    
    # Сравниваем линейный и бинарный поиск по баллу
    print(f"\nИщем студентов с баллом: {search_grade}")
    
    # Линейный поиск по баллу
    start_time = time.time()
    grade_results_linear = search_system.search_by_grade_linear(search_grade)
    linear_grade_time = time.time() - start_time
    
    # Бинарный поиск по баллу
    start_time = time.time()
    grade_results_binary_2 = search_system.binary_search_by_grade(search_grade)
    binary_grade_time = time.time() - start_time
    
    print(f"\nЛинейный поиск по баллу:   {linear_grade_time:.6f} сек")
    print(f"Бинарный поиск по баллу:    {binary_grade_time:.6f} сек")
    print(f"Разница:                    {linear_grade_time/binary_grade_time:.1f}x")
    print(f"\nОба метода нашли одинаковое количество студентов: {len(grade_results_linear) == len(grade_results_binary_2)}")
    
    # Демонстрация поиска несуществующего студента
    print("\n" + "="*70)
    print("ПОИСК НЕСУЩЕСТВУЮЩЕГО СТУДЕНТА")
    print("="*70)
    fake_name = "Иван Несуществующий"
    fake_grade = 99.99
    
    start_time = time.time()
    fake_results = search_system.linear_search_by_name(fake_name)
    time_fake = time.time() - start_time
    print(f"Поиск по имени ('{fake_name}'): {len(fake_results)} результатов, время: {time_fake:.6f} сек")
    
    start_time = time.time()
    fake_grade_results = search_system.binary_search_by_grade(fake_grade)
    time_fake_grade = time.time() - start_time
    print(f"Поиск по баллу ({fake_grade}): {len(fake_grade_results)} результатов, время: {time_fake_grade:.6f} сек")

def additional_tests():
    """Дополнительные тесты производительности"""
    print("\n" + "="*70)
    print("ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ НА РАЗНЫХ РАЗМЕРАХ ДАННЫХ")
    print("="*70)
    
    sizes = [100, 1000, 5000, 10000]
    
    print(f"\n{'Размер':<10} {'Линейный поиск':<20} {'Бинарный поиск':<20} {'Ускорение':<10}")
    print("-" * 60)
    
    for size in sizes:
        # Генерируем студентов
        students = generate_students(size)
        search_system = StudentSearchSystem(students)
        
        # Выбираем случайный балл для поиска
        target_grade = random.choice(students).grade
        
        # Линейный поиск
        start = time.time()
        linear_results = search_system.search_by_grade_linear(target_grade)
        linear_time = time.time() - start
        
        # Бинарный поиск
        start = time.time()
        binary_results = search_system.binary_search_by_grade(target_grade)
        binary_time = time.time() - start
        
        speedup = linear_time / binary_time if binary_time > 0 else 0
        
        print(f"{size:<10} {linear_time:<20.6f} {binary_time:<20.6f} {speedup:<10.1f}x")

if __name__ == "__main__":
    # Основная демонстрация
    demo_search_system()
    additional_tests()