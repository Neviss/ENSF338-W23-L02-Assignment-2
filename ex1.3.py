retrival = {}

def memoization(n):
    if (n == 0) or (n == 1):
        return n
    else:
        if n not in retrival:
            retrival[n] = memoization(n-1) + memoization(n-2)
        return retrival[n]