class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maps={}
        result=[]
        for number in nums:
            maps[number]=1
        for i in range(1,len(nums)+1):
            if i not in maps.keys():
                result.append(i)
        return result
