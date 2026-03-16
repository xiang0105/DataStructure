# 1.
# 用 for 迴圈寫出九九乘法表，從 1 x 1 = 1 到 9 x 9 = 81

# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")

# 2.
# ls1 = [1, 2, 3, 4]
# for i in range(len(ls1)):
#     p = ls1.pop()
#     ls1.append(p)
# print(ls1)

# pop 移除陣列最後一個元素，並回傳該元素的值
# ---
# [1,2,3,4]

# 3.
# ls1 = 'admin'
# for char in ls1:
#     if char == 'm':
#         continue
#     print(char)

# continue 跳過當前迴圈的剩餘部分，直接進入下一次迴圈的判斷
# ---
# a 
# d
# i
# n

# 4.
# var = 10
# while var:
#     var -= 1
#     if var > 5:
#         continue
#     print(var)

# ---
# 5
# 4
# 3
# 2
# 1
# 0

# 5.
# 給定 list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]，請問如何使用索引 (slice) 拿到整數 6000 ?

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# print(list1[2][2][1])

# 6.
# 寫一個使用 if-elif-else 與 input 的程式，程式功能要能夠判斷 input 的值是不是 5 的倍數，如果是就 print 'Yes!'，否則就 'No!'。

# inp = int(input())
# if inp % 5 == 0:
#     print('Yes!')
# else:    
#     print('No!')

# 7.
# 透過for完成15"*"的三角形中心為7"*"

# for i in range(8 , 0 , -1):
#     if i > 1:
#         print(" " * (i - 1) + "*" * i)
#     else:
#         print("*")

#8.

# for i in range(1 , 7):
#     for j in range(1 , i):
#         print(j , end=" ")
#     print()

#9.
# a = 4
# while a < 8:
#     print(a)
#     a += 1
    
#10.
# ls1 = []
# while len(ls1) < 4:
#     num = int(input())
#     if num % 2 == 0:
#         ls1.append(num)
# print(ls1)