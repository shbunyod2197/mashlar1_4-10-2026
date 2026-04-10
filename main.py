# 1
roy = [5, 55, 99, 7, 6]

x = list(map(lambda a: a ** 2, roy))
print(x)
# 2
roy = [5, 55, 99, 7, 6]

x = list(map(lambda a: a ** 2, roy))
print(x)

# 3
roy = ['apple', 'banana']

x = list(map(lambda a: a.upper(), roy))
print(x)

# 4
roy = ['salom']

x = list(map(lambda a: len(a), roy))
print(x)

# 5
roy = [3, 8, 9]
roy1= [4, 8, 7]

x = list(map(lambda a, b: a + b, roy, roy1))
print(x)

# 6
roy = [9, 10, 99]
print(roy)

x = list(map(lambda a: abs(a), roy))
print(x)

# 7
roy = ['borxuS', 'molaS']
print(roy)

x = list(map(lambda a: a[::-1], roy))
print(x)

# 8
roy = [3, 6, 9]
print(roy)

x = list(map(lambda a: a ** 3,roy))
print(x)

# 9
roy = ['salom', 'Avlik']
print(roy)

x = list(map(lambda a: a[0], roy))
print(x)

# 10
roy = [1, 2, 3]
print(roy)

x = list(map(lambda a: a % 2 == 0, roy))
print(x)

# 11
roy = [3, 7, 6]
print(roy)

roy2 = [1 ,2 ,3]

x = list(map(lambda a: a ** 2, roy))
print(x)

# 12
roy = ['abas', 'absd']
print(roy)


x = list(map(lambda a: a.abs, roy))
print(x)

# 13
n = int(input("Son kirt: "))
roy = [n]

x = list(map(lambda a: a ** n, roy))
print(x)

# 14
roy = ['Your', 'Name']
print(roy)


x = list(map(lambda a: a + '!', roy))
print(x)

# 15
roy = [1, 2, 3]
print(roy)

roy2 = [1, 2, 3]
print(roy2)

roy3 = [1, 2, 3]
print(roy3)

x = list(map(lambda a, b, c: a + b + c, roy, roy2, roy3))
print(x)

# 16
roy = [1.3, 3, 8.9, 9.9999999999999999]
print(roy)


x = list(map(lambda a: int(a), roy))
print(x)

# 17
roy = ['Bunyod', 'SBRZS']
print(roy)


x = list(map(lambda a: a.lower(), roy))
print(x)

# 18
roy = [1, 24, 3]
print(roy)


x = list(map(lambda a: a * 100 and f"{a}%", roy))
print(x)

# 19
roy = ['appkle', 'banana']
print(roy)


x = list(map(lambda a: a[-1], roy))
print(x)

# 20
roy = [2, 5, 9]
print(roy)


x = list(map(lambda a: bin(a), roy))
print(x)
