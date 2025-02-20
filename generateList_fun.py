import random
def generate_list(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 100))
    return result
print(generate_list(20))