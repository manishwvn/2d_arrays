def wave_traversal(arr):
    # i represents columns, j represents rows
    # the idea is to traverse through columns, 
    # if column is odd, traverse down
    # if column is even, traverse up
    for i in range(len(arr[0])):
        
        if i % 2 == 0:
            for j in range(len(arr)):
                print(arr[j][i])
        else:
            for j in range( len(arr) - 1, -1, -1):
                print(arr[j][i])


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
wave_traversal(arr)

'''
     j
i    1 2 3 4 
     5 6 7 8 
     9 10 11 12
'''