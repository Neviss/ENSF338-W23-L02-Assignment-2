import sys
import matplotlib.pyplot as plt
import numpy as np
import json
import time



sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
    else:
        return

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


data = {}
timeData = {}

with open('ex2.json', 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)




count = 0
for i in data:
    print(len(i))
    start = time.time()
    place = func1(i, 0, int(len(i)) - 1)
    end = time.time()
    interval = end - start
    timeData[interval] = len(i)
    print(timeData)
    count += 1


    


keys = list(timeData.keys())
values = list(timeData.values())

# Create the bar chart
plt.plot(keys, values, color='r')

# Add labels and title

plt.xlabel('Time')
plt.ylabel('Array Size')
plt.title('Time Complexity of Bubble Sort')

# Show the plot
plt.show()