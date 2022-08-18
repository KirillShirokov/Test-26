rep = []

b = "Hello"
a = []
for letters in b:
    a.append(letters)

a.sort()
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        rep.append(a[i])

rep = list(set(rep))
print(rep)