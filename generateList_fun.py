import random
def generate_list(n):
    return [random.randint(1, 100) for i in range(n)]
print(generate_list(20))