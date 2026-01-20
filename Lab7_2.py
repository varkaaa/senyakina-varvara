def main():
    # Запрашиваем количество коробок
    print("Введите количество коробок: ")
    line = input().split()
    if not line:
        return
    n = int(line[0])

    # Список для хранения характеристик коробок: (вес, прочность)
    presents = []
    for i in range(n):
        # Считываем вес и то, какой вес сверху может выдержать коробка (прочность)
        weight, strength = map(int, input().split())
        presents.append([weight, strength])

    # Сортируем коробки по правилу: вес + прочность
    # Это позволяет найти оптимальный порядок, чтобы самые "выносливые" были снизу
    presents.sort(key=lambda x: x[0] + x[1])

    # Общий вес всех коробок, которые мы уже поставили СВЕРХУ на текущую
    current_total_weight = 0
    # Количество успешно поставленных коробок
    count = 0

    # Проходим по списку коробок
    for box in presents:
        weight = box[0]
        strength = box[1]

        # Если прочность текущей коробки позволяет выдержать вес всех коробок над ней
        if current_total_weight <= strength:
            # Увеличиваем счетчик
            count = count + 1
            # Добавляем вес этой коробки в общую копилку веса
            current_total_weight = current_total_weight + weight

    # Выводим результат
    print("Количество сложенных друг на друга коробок:", count)

if __name__ == "__main__":
    main()