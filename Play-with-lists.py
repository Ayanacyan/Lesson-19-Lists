L=[4, 6, 7, 9, 44, 37, 23, 16, 69]
print("Original List", L)

count=0

for i in L:
    count+=i


avg=count/len(L)
print("sum= ", count)
print("average= ", avg)

L.sort()

print("Smallest element is: ", L[0])

print("Largest Element is: ", L[-1])