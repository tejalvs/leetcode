def Solution(arr):
    size=len(arr)
    count0=0
    count1=0
    for i in range(0,size):
        if arr[i]==0:
            count0+=1
        else:
            count1+=1

    for i in range(0,count0):
        arr[i]=0

    for i in range(count0,size):
        arr[i]=1

    print(arr)


Solution([1,0,0,1,1,0,1,1,0,1,0,1,0])