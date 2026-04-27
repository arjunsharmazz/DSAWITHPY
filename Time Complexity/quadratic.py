a=9
print(a)
for i in range(a):
    for j in range(a):
        print(i,j,end=" ")
        # print(i,j)
        # this is quadratic time complexity O(n^2) because the time taken to execute increases quadratically with the size of the input.