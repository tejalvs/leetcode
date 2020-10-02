class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        if len(nums) == 1: return 1
        j = 1 
        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1]: 
                nums[j] = nums[i]
                j += 1
      
        return j
        '''j = 1
        i = 0
        while(j<len(arr)):
            if arr[i] == arr[j]:
                j+=1
            else:
                i+=1
                arr[i] = arr[j]
                j+=1
        arr = arr[0:i+1]
        return i+1'''
      
