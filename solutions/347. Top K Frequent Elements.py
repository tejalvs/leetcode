class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result={}
        finalList=[]
        nums.sort
        for i in nums:
            if i in result:
                result[i]+=1
            else:
                result[i]=1
        result1=sorted(result.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
        finalList=[]
        for i in range(k):
            finalList.append(result1[i][0])
        return finalList
                
        
