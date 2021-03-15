def fibSeq(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibSeq(n-1) + fibSeq(n-2)


print(fibSeq(20))
