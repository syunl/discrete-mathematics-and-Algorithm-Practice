# def addUpTo(number):
#     if number == 1:
#         return 1
#     else:
#         return number + addUpTo(number-1)


# a = addUpTo(100)
# print(a)

# an = 2 * an-1 + 7, a1 = 1


def recSeq(n):
    if n == 1:
        return 1
    else:
        return 2 * recSeq(n-1) + 7


print(recSeq(5))
