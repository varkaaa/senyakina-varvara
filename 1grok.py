ЗАДАНИЕ 1
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def generate_random_array(size):
    return [random.randint(2, 103) for _ in range(size)]

def main():
    arr = generate_random_array(random.randint(5, 25))
    print("До сортировки:", arr)
    print("После сортировки:", selection_sort(arr.copy()))

if __name__ == "__main__":
    main()


ЗАДАНИЕ 2

import random

def generate_random_array(size):
    return [random.randint(0, 100) for _ in range(size)]

def sort_reverse(arr):
    return sorted(arr, reverse=True)

def main():
    arr = generate_random_array(random.randint(5, 25))
    print("До сортировки:", arr)
    print("После сортировки:", sort_reverse(arr))

if __name__ == "__main__":
    main()

ЗАДАНИЕ 3

import random

def generate_random_phones(size):
    return [f"{random.randint(0, 99):02d}-{random.randint(0, 99):02d}-{random.randint(0, 99):02d}" for _ in range(size)]

def sort_phone(phones):
    phonesarr = [(int(p.replace('-', '')), p) for p in phones]
    n = len(phonesarr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if phonesarr[j][0] < phonesarr[min_index][0]:
                min_index = j
        phonesarr[i], phonesarr[min_index] = phonesarr[min_index], phonesarr[i]
    return [p[1] for p in phonesarr]

def main():
    phones = generate_random_phones(random.randint(5, 25))
    print("До сортировки:", phones)
    print("После сортировки:", sort_phone(phones))

if __name__ == "__main__":
    main()
