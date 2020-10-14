def puh(*m):
    a = [sum(x in 'уеыаоэяию' for x in i) for i in m]
    return 'Парам пам-пам' if all(a[0] == i for i in a) else 'Пам парам'


print(puh(*input().split()))
