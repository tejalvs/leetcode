class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        if(len(left)==0 ):
            return abs(n-min(right))
        elif(len(right)==0 ):
            return abs(0-max(left))
        else:
            maxLeft=max(left)
            maxRight=min(right)
        print(maxRight,maxLeft)
        
        return(max((abs(n-maxRight)),abs(0-maxLeft)))
        
        
        '''      
        BestRightDistance=0
        BestLeftDistance=0
        
        for i in range(0,len(right)):
            #print(right[i],n,n-right[i])
            displacement=n-right[i]
            if (displacement>BestRightDistance):
                BestRightDistance=displacement
       
        for j in range(0,len(left)):
            print(left[j],n,n-left[j])
