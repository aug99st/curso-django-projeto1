import random

number = list(range(0,11))
number= random.choice(number)
print(number)
second_number = random.choice(range(0,11))
if number == second_number:
    print(f'aleatorios nao aleatorios kkk {second_number}')