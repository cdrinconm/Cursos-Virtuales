
def minRefills(stations,n,L):
	numRefills = 0
	currentRefill = 0
	while currentRefill <= n:
		lastRefill = currentRefill
		while (currentRefill <= n) and (stations[currentRefill+1] - stations[lastRefill] <= L):
			currentRefill = currentRefill + 1		
		if currentRefill == lastRefill:
			return -1
		if currentRefill <= n:
			numRefills = numRefills + 1
	return numRefills


b = int(input())
capacity = int(input())
numstations = int(input())

stations = [int(x) for x in input().split()]
stations.insert(0,0)
stations.append(b)

#print(values)
print(minRefills(stations,numstations,capacity))
	