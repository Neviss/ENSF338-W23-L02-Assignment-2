import time
import matplotlib.pyplot as plt

retrival = {}

def memoization(n):
    if (n == 0) or (n == 1):
        return n
    else:
        if n not in retrival:
            retrival[n] = memoization(n-1) + memoization(n-2)
        return retrival[n]

def func(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return func(n-1) + func(n-2)

memoTime = []
funcTime = []
numi = []

for i in range(36):
    start = time.time()
    memoization(i)
    end = time.time()
    memoTime.append(end-start)

    start1 = time.time()
    func(i)
    end1 = time.time()
    funcTime.append(end1-start1)
    numi.append(i)

figure = plt.figure()
funcT = figure.add_subplot(111)
funcT.scatter(numi, memoTime, c="b", label="With memoization", alpha=0.5)
funcT.scatter(numi, funcTime, c="r" ,label="Without memoization", alpha=0.5)

plt.legend()
plt.xlabel("ith fibinochi number")
plt.ylabel("Time (s)")
plt.show()