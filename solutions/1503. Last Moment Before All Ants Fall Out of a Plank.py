class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        BestRightDistance=0
        BestLeftDistance=0
        
        for i in range(0,len(right)):
            #print(right[i],n,n-right[i])
            displacement=n-right[i]
            if (displacement>BestRightDistance):
                BestRightDistance=displacement
       
        for j in range(0,len(left)):
            print(left[j],n,n-left[j])
            displacement=abs(0-left[j])
            if (displacement>BestLeftDistance):
                BestLeftDistance=displacement
    
    
    
        return max(BestRightDistance,BestLeftDistance)
