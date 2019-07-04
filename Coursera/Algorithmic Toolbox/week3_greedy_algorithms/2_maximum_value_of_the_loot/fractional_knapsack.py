
def optimal_value(capacity,values):
	maximum = 0
	while  capacity !=0:
		mayor = 0
		i=0
		for i in range(len(values)):
			if values[i][0] > values[mayor][0]:
				mayor = i
		if capacity > values[mayor][1]:
			maximum = maximum + (values[mayor][0]*values[mayor][1])
			capacity = capacity - values[mayor][1]
			values.pop(mayor)
		else:
			maximum = maximum + (values[mayor][0]*capacity)
			capacity = 0
	return maximum


enter = [int(x) for x in input().split()]
values = []

for i in range(enter[0]):
	array = [int(x) for x in input().split()]
	values.append([array[0]/array[1],array[1]])

#print(values)
print(optimal_value(enter[1],values))
