import heapq

def main():
    # Считываем количество вершин, начало и конец пути
    data = input().split()
    if not data: return
    N = int(data[0])
    S = int(data[1])
    F = int(data[2])

    # Считываем матрицу (таблицу расстояний)
    matrix = []
    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
        # Выводим строку, как в оригинальной программе
        for value in row:
            print(value, end=" ")
        print()

    # Заменяем бесконечность большим числом
    infinity = 10**9
    distances = [infinity] * N
    
    # Стартовая вершина (корректируем индекс на -1)
    start_node = S - 1
    end_node = F - 1
    distances[start_node] = 0

    # Очередь: (расстояние, вершина)
    pq = [(0, start_node)]

    while len(pq) > 0:
        current_dist, u = heapq.heappop(pq)

        # Если нашли путь короче ранее, игнорируем старый вариант
        if current_dist > distances[u]:
            continue

        # Перебираем все возможные города 'v', чтобы найти соседей
        for v in range(N):
            weight = matrix[u][v]
            
            # Если в таблице не -1, значит дорога существует
            if weight != -1:
                new_dist = distances[u] + weight
                
                # Если нашли путь короче
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

    # Итоговый вывод
    ans = distances[end_node]
    if ans == infinity:
        print("Кратчайший путь до конечной вершины = -1")
    else:
        print("Кратчайший путь до конечной вершины =", ans)

main()

"""
тестовые данные:
4 1 4
0 4 -1 -1
-1 0 2 6
-1 -1 0 2
-1 -1 -1 0
Результат: 8

"""
