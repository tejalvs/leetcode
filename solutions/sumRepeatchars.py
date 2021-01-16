def sumVal(arr):
    n=len(arr)
    total=sum(arr)-(((n-1)*n)//2)
    print(sum(arr),n,total)


sumVal([1,2,3,4,4])