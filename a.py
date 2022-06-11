import random
print(random.uniform(0, 1))


a = [1,0,1,0,1]
b = [0,0,1,1,1]

split = len(a)//2
print(a[:split])
print(a[split:])

print(a[:split] + b[split:])
