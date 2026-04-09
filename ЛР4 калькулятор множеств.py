def set_calculator():
    """
    Интерактивный калькулятор множеств A и B из файлов
    """
    print("Калькулятор множеств и реляционная алгебра")

    # ввод путей к файлам
    path1 = input("Введите путь к первому файлу (setA.txt): ").strip()
    if not path1:
        path1 = "setA.txt"

    path2 = input("Введите путь ко второму файлу (setB.txt): ").strip()
    if not path2:
        path2 = "setB.txt"

    print(f"\nЧитаем файлы: {path1}, {path2}")

    # функция чтения множества
    def read_set(filename):
        s = set()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    item = line.strip()
                    if item:
                        s.add(item)
                    else:
                        print(f"Пропущена пустая строка {line_num} в {filename}")
            print(f"Из {filename} загружено {len(s)} уникальных элементов")
            return s
        except FileNotFoundError:
            print(f"Файл {filename} не найден! Создайте его.")
            return set()
        except Exception as e:
            print(f"Ошибка при чтении {filename}: {e}")
            return set()

    # загружаем множества
    a = read_set(path1)
    b = read_set(path2)

    if not a or not b:
        input("Нажмите Enter для выхода...")
        return

    print(f"\nМножество A: {sorted(a)}")
    print(f"Множество B: {sorted(b)}")
    print("-" * 50)

    # меню операций
    while True:
        print("\nОперации множеств (реляционная алгебра):")
        print("1. Объединение      A ∪ B  |  UNION")
        print("2. Пересечение      A ∩ B  |  INTERSECT")
        print("3. Разность         A - B  |  DIFFERENCE")
        print("4. Обратная разность B - A")
        print("5. Симм. разность   A Δ B  |  SYMMETRIC DIFF")
        print("6. Равенство        A == B")
        print("0. Выход")

        cmd = input("Выберите операцию (0-6): ").strip()

        if cmd in ('0', 'exit', 'выход', 'q'):
            print("\nПрограмма завершена.")
            break

        elif cmd == '1':
            res = a | b
            print(f"A ∪ B = {sorted(res)}")
            print(f"Количество элементов: {len(res)}")

        elif cmd == '2':
            res = a & b
            print(f"A ∩ B = {sorted(res)}")
            print(f"Количество элементов: {len(res)}")

        elif cmd == '3':
            res = a - b
            print(f"A - B = {sorted(res)}")
            print(f"Количество элементов: {len(res)}")

        elif cmd == '4':
            res = b - a
            print(f"B - A = {sorted(res)}")
            print(f"Количество элементов: {len(res)}")

        elif cmd == '5':
            res = a ^ b
            print(f"A Δ B = {sorted(res)}")
            print(f"Количество элементов: {len(res)}")

        elif cmd == '6':
            print(f"Множества {'равны' if a == b else 'различаются'}")
            if a != b:
                print(f"Только в A: {sorted(a - b)}")
                print(f"Только в B: {sorted(b - a)}")
        else:
            print("Ошибка! Введите число от 0 до 6")

    input("\nНажмите Enter для выхода...")


# запуск программы
if __name__ == "__main__":
    set_calculator()