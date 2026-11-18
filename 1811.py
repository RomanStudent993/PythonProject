print("hello world")
#str
#int
#flout
#list
#tuple
#bool
#set
#dict

#None

N = int(input())
a = 0
b = 0

for i in range(N):
    value = int(input())
    if i % 2 == 0:
        a += value
    elif i % 2 == 1:
        b += value

c = a - b
print(c)