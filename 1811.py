# # # R = int(input())
# # # C = int(input())
# # # summ = 0
# # #
# # # for i in range(R):
# # #     for j in range(C):
# # #         value = int(input())
# # #         new_number = j * R + i + 1
# # #         summ += value * new_number
# # # print(summ)
# #
# #
# #
# # N = int(input())
# #
# # best_summ = -1
# # best_name = ""
# # for i in range(N):
# #     name = input()
# #     summ = 0
# #     for _ in range(3):
# #         a = int(input())
# #         summ += a
# #
# #     if summ > best_summ:
# #         best_summ = summ
# #         best_name = name
# # print(best_name)
#
#
# A = int(input())
# B = int(input())
# M = int(input())
#
# nod = 1
# for i in range(2, 1001):
#     if A % i == 0 and B % i == 0:
#         nod = i
# nok = A * B // nod
# total = 0
# for i in range(nok, M + 1, nok):
#     total += i
# # print(total)
#
#
# N = int(input())
# max_value = 0
# second = 0
# for i in range(N):
#     value = int(input())
#     if value > max_value:
#         second = max_value
#         max_value = value
#     elif max_value > value and value > second:
#         second = value
# print(second)