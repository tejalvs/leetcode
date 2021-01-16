#Given a 2d sorted array of 0 and 1 find the row with the most 1s.
def count(arr):
    max_row=0
    for i in arr:
        i.sort()
    j=arr[0].index(1)
    print(j)




count([[1,1,1,1,0],[0,0,0,0,0],[1,1,1,1,1],[0,1,0,0,1]])