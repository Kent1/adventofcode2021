# Part 1
with open("input.txt", 'r') as f:
    numbers = [int(number) for number in f.readlines()]
    print(len(list(filter(lambda x : x[1]-x[0] > 0, zip(numbers, numbers[1:])))))

# Part 2
with open("input.txt", 'r') as f:
    numbers = [int(number) for number in f.readlines()]
    sums = [sum(numbers[i:i+3]) for i in range(len(numbers))]
    print(len(list(filter(lambda x : x[1]-x[0] > 0, zip(sums, sums[1:])))))
