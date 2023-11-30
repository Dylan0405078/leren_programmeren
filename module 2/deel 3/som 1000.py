# som > 1000

total = 0
number = 50
iteration = 1

while total <= 1000:
    total += number
    print(f"{iteration}. {'+'.join(map(str, range(50, number+1)))} = {total}")
    number += 1
    iteration += 1
