# Page 3
arr = [1, 4, 1, 4, 2, 1, 3, 5, 6]

x = int(input("Enter the value:"))

res = []
for n in arr:
    if n >= x:
        res.append(n)

print(res)