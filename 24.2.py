import sys

words = sorted(sys.stdin.read().split())
sort = {}
for word in words:
    summa = 0
    for letter in word:
        summa = summa + ord(letter.upper()) - ord("A") + 1
    sort[word] = summa
for element in sorted(sort, key=sort.get):
    print(element)
