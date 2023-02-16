import sys
import matplotlib.pyplot as plt
import numpy as np
import json
import time


sys.setrecursionlimit(20000)
def func1(array, low, high):

    if low < high:
        spot = func2(array, low, high)

        func1(array, low, spot - 1)

        func1(array, spot + 1, high)

def func2(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1 
 
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