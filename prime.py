
# 判斷是否為質數
def isPrime(num):
    starter = 2
    while (starter < num):
        if (num % starter == 0):
            return False
        starter += 1
    return True

# 找到第nth個質數


def nthPrime(nth):
    starter = 2
    primeList = []
    while (len(primeList) < nth):
        if (isPrime(starter)):
            primeList.append(starter)
        starter += 1
    return primeList[-1]


def nthPrime2(nth):
    starter = 7
    primeList = [2, 3, 5]
    while (len(primeList) < nth):
        isPrime = True
        for n in primeList:
            if (starter % n == 0):
                isPrime = False
        if (isPrime):
            primeList.append(starter)
        starter += 2
    return primeList

# Prime Factorization


def factorPrime(num):
    primeList = nthPrime2(num)
    factor = []
    for i in primeList:
        if (num % i == 0):
            factor.append(i)
    return factor


def factorPrime_answer(num):
    answer = []
    n = 2
    while num > 1:
        if (num % n == 0):
            if n not in answer:
                answer.append(n)
            num /= n
        else:
            n += 1
    return answer


print(factorPrime_answer(120))
print(factorPrime_answer(170))
