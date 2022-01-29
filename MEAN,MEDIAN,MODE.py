from collections import Counter
from tkinter import W
import math
from numpy import median
import statistics
import csv 

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

print("\nGetting Mean")
n = len(new_data)
total = 0
for x in new_data:
    total += x
mean = total/n
print('Mean is: '+str(round(mean, 6)))

print("\nGetting Median")
n = len(new_data)
new_data.sort()
if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]
print("Median is: "+str(median))

# print("\nGetting Mode")
# data = Counter(new_data)
# mode_data_for_range = {
#     "100-110":0,
#     "110-120":0,
#     "120-130":0,
# }
# for weight,occurrence in data.items():
#     if 100<float(weight)<110:
#         mode_data_for_range["100-110"]+=occurrence
#     elif 110<float(weight)<120:
#         mode_data_for_range["110-120"]+=occurrence
#     elif 120<float(weight)<130:
#         mode_data_for_range["120-130"]+=occurrence
# mode_range,mode_occurrences = 0,0
# for range,occurrence in mode_data_for_range.items():
#     if occurrence>mode_occurrences:
#         mode_range, mode_occurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence
#         mode = float((mode_range[0] + mode_range[1]) / 2)
#         print(f"Mode is -> {mode:2f}")

print("\nGetting Mode")
data = new_data
datas = [math.floor(num) for num in data]
print("Mode is: %s"%statistics.mode(datas))
