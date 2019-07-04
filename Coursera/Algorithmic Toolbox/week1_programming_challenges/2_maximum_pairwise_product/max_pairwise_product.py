
n = int(input())
numbers = [int(x) for x in input().split()]

max_index1 = -1
for i in range(n):
    if max_index1 == -1 or numbers[i] > numbers[max_index1]:
        max_index1 = i

max_index2 = -1
for j in range(n):
    if j != max_index1 and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
        max_index2 = j

print (numbers[max_index1]*numbers[max_index2])