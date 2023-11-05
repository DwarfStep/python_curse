from numpy import *

# 1 point
s = ''


def leng(string):
    return len(string)


print(leng(s))
# 2 point


def lists(list1, list2):
    leng = max(len(list1), len(list2))
    print(leng)


a1 = [1, 2, 3]
a2 = ["1", "2", "23", "4", "5"]
lists(a1, a2)
# 3 point


def sum_list(list1, sim1):
    list1.append(sim1)
    print(list1)


sim = 1
sum_list(a1, sim)

# 4 point


def number_separator(num):
    if num < -100 or num > 100:
        print('-')
    else:
        print('+')


number_separator(100)

# 5 point


def number_separator(num):
    if num < -100 or num > 100:
        print('-')
    else:
        print('+')


number_separator(100)


def str_detector(str1, str2):
    if str1 in str2:
        print("ДА")
    else:
        print("НЕТ")


str_detector('test', 'test1')
# 6 point


def positive_number(nums):
    a = [i for i in nums if i > 0]
    print(len(a))


positive_number([1, -1, 5, 4, -5])


# 7 point


def days(num1, num2):
    sumat = (num1*12+num2)*29
    print(sumat)


days(1, 5)
# 8 point


# 1 вариант, не очень понятно что подразумевалось по исключением
def str_out(str1):
    if type(str1) is str:
        print(*[i[0] for i in str1.split()], sep='')
    else:
        print(str1)


str_out('absa cad fda')
# 2 идея правильности задания


def str_out1(str1):
    try:
        print(str1+'ss')
    except Exception as ex:
        print(ex)
    else:
        print(*[i[0] for i in str1.split()], sep='')


str_out1(24)
# 9 point


def factar(num1):
    c= 1
    for i in range(1, num1+1):
        c *= i
    print(c)


factar(4)

# 10 point
lst = [2, 4, 5, 8, 9, 13]
# 1 метод
lst1 = [i*lst.index(i) for i in lst]
# 2 метод
i = 0
while i < len(lst):
    lst[i] *= i
    i += 1
print(lst)
print(lst1)

