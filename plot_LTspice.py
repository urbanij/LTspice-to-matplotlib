import sys
import math
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME = sys.argv[1]

with open(FILE_NAME, "r") as f:
	first_row = f.readline()
# print (first_row)


my_data = np.genfromtxt(FILE_NAME, delimiter='\t')

x = []
y = []
for i in range(len(my_data)):
	# check if number
	x1 = float(my_data[i][0])
	y1 = float(my_data[i][1])	
	if not (math.isnan(x1) or math.isnan(y1)):
		x.append(x1)
		y.append(y1)


print ("mean = %f" %(np.mean(y)))


# plotting
plt.plot(x,y)
if math.isnan(my_data[0][0]) and math.isnan(my_data[0][1]):
	plt.xlabel(first_row.split('\t')[0])
	plt.ylabel(first_row.split('\t')[1][:-1])
plt.grid(True)
plt.show()