a=9
print(a)
for i in range(a):
    for j in range(a):
        for k in range(a):
            print(i,j,k,end=" ")
            # print(i,j,k)
            # this is cubic time complexity O(n^3) because the time taken to execute increases cubically with the size of the input.