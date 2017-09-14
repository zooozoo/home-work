# 1번 문제
def number1(a):
    # 2번 문제
    'Maching color with fruits'
    if a =='red':
        print('apple')
    elif a=='yellow':
        print('banana')
    elif a=='green':
        print('melon')
    else:
        print("I don't know")

result = number1('red')

help(number1)

# 3번 문제
def multi(*args):
    if len(args) <=  1:
        print(args[0]**2)
    elif len(args) == 2:
        print(args[0]*args[1])

# 4번 문제
def number4(a, b):
    summer = a + b
    minus = a - b
    return(summer,minus)

print(number4(2,3))

# 5번 문제
def number5(*args):
    print(len(list(args)))

print(number5(1,2,3,4))


# 6번 문제

[print('{}x{}={}'.format(i, a, i*a), end='\t') for i in range(2, 10) for a in range(1, 10) ]
