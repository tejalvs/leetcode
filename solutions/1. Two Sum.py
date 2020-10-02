class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(0,len(nums)):
            map[nums[i]]=i
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if((rem in map.keys()) and (map[rem]!=i)):
                return [map[rem],i]
            
