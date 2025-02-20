import random
def generate_list(n):
<<<<<<< HEAD
    return [random.randint(1, 100) for i in range(n)]
=======
    result = []
    for i in range(n):
        result.append(random.randint(1, 100))
    return result
>>>>>>> a35e432 (Функция с поэлементным заполнением списка)
print(generate_list(20))