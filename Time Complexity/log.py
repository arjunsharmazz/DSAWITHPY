a=90
print(a)
for i in range(a):
    print(i,end=" ")
    a=a//2
    # print(i)
    # this is logarithmic time complexity O(log n) because the time taken to execute increases
    # code output increases logarithmically with the size of the input.
    # exmle 90 -> 45 -> 22 -> 11 -> 5 -> 2 -> 1 -> 0
    