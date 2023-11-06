def sort_condition(num):
    return len(num), num

n = int(input())
words = []
for i in range(n):
    words.append(input())

words = list(set(words))
words.sort(key=sort_condition)

for i in words: print(i)