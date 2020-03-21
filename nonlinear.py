from scipy.misc import derivative


def func(x):
    return (x ** 3) - 2 * (x ** 2) - 4 * x - 7


def bir(lower=3, upper=4, ep=1e-5):
    if func(lower) * func(upper) > 0:
        return None, 0
    if func(lower) > 0 > func(upper):
        lower, upper = upper, lower

    global countb
    countb += 1
    mid = (upper + lower) / 2
    # print('recurring...now:', mid)
    if upper - lower <= ep:
        return mid, countb
    x = func(mid)
    if x < 0:
        return bir(mid, upper, ep)
    elif x > 0:
        return bir(lower, mid, ep)
    elif x == 0:
        return mid, countb


def bic(lower=3, upper=4, ep=1e-5, time=50):
    if func(lower) * func(upper) > 0:
        return None, 0
    if func(lower) > 0 > func(upper):
        lower, upper = upper, lower
    for counter in range(1, time + 1):
        mid = (lower + upper) / 2
        # print('finding...', mid)
        if func(mid) == 0 or upper - lower <= ep:
            return mid, counter
        if func(mid) > 0:
            lower, upper = lower, mid
        elif func(mid) < 0:
            lower, upper = mid, upper


def newton(x=4, ep=1e-5, time=50):
    x2 = x - func(x) / derivative(func, x, dx=1e-6)
    global countn
    countn += 1
    if abs(x - x2) <= ep:
        return x2, countn
    elif countn >= 50:
        raise ValueError
    return newton(x2)


if __name__ == '__main__':
    countb = countn = 0
    result, counts = bir()
    print('Binary: {} time recursion, The answer is: {}'.format(counts, result))
    result, counts = bic()
    print('Binary: {} time cycle, The answer is: {}'.format(counts, result))
    result, counts = newton()
    print('Newton: {} time recursion, The answer is: {}'.format(counts, result))
