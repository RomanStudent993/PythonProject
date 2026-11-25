# break
# continue
# else


#==================================================

### break
# for i in range(10):
#     print(i)
#     if i == 5:
#         break

#==================================================

### flag
# count = 0
# flag = True
# while flag:
#     if count == 5:
#         flag = False
#     count += 1
#     print(count)

#==================================================

### continue
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

### continue
# count = 0
# for i in range(10):
#     if i == 2:
#         count += 2
#         continue
#     if i % 2 == 0:
#         count += 1

#==================================================

### else
# i = 0
# while i < 3:
#     print(i)
#     i += 1
#     if i == 2:
#         break
# else:
#     print("Цикл завершился нормально")

### else
# i = 1
# while i < 200:
#     if i % 7 == 0:
#         print(i)
#         break
# else:
#     print("Такое число не найдено")


#==================================================
#==================================================

### Задачи:

# 1 задача

# N = int(input())
# password = "qwerty2024"
#
# for i in range(N):
#     a = input()
#     if a == password:
#         print("Доступ")
#         break
# else:
#     print("Отказ")


# 2 задача

# A = int(input())
# B = int(input())
#
# for i in range(A, B+1):
#     if i % 7 == 0:
#         print(i)
#         break
# else:
#     print(0)


# 3 задача

# N = int(input())
# summ = 0
#
# for i in range(N):
#     a = int(input())
#     if a >= 60:
#         summ += a
#     else:
#         continue
#
# print(summ)


# 4 задача

# N = int(input())
#
# for i in range(2, N):
#     if N % i == 0:
#         print(i)
#         break
# else:
#     print(0)


# 5 задача

# N = int(input())
# rub = 1000
# count = 0
#
# while count < N:
#     num = int(input())
#     if rub - num < 0:
#         print("Отклонено")
#         break
#     rub -= num
#     count += 1
# else:
#     print("Выполнено")


# 6 задача

# N = int(input())
# summ = 0
#
# for i in range(N):
#     age = int(input())
#     if age >= 18:
#         summ += age
#     else:
#         continue
# print(summ)


# 7 задача

# N = int(input())
#
# for i in range(N):
#     a = int(input())
#     if a < 0:
#         print(i+1)
#         break
# else:
#     print(0)
