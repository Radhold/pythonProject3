def partial_sums(*args):
    a = [0]
    for i, x in enumerate(args):
        a.append(x + a[i])
    return a


print(partial_sums(1, 0.5, 0.25, 0.125))
