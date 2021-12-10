l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_number(num):

    return num % 2 == 0


even = list(filter(even_number, l1))

print(even)
