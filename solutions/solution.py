def plusOne():
        A=[0]
        multiple=1
        org_no=0
        B=[]
        print(len(A))
        for number in range(len(A)-1,-1,-1):
            org_no=org_no+A[number]*multiple
            multiple=multiple*10
            print(org_no)
        
        result=org_no+1
        print(result)
        while(result>0):
            digit=result%10
            result=result//10
            B.insert(0,digit)
        print(B)

def wave():
    A=[1, 4, 3, 2,5]#1,2,3,4,5
    A.sort()
    for i in range(0,len(A),2):
        if i!=0:    
            A[i],A[i-1]=swap(A[i],A[i-1])
    print(A)


def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b    




wave()
        