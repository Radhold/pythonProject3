def swap(x, y):
    x[:], y[:] = y[:], x[:]


first = [1, 2, 3]
second = [4, 5, 6, 7]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
