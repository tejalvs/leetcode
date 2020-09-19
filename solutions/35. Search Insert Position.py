class Solution:
    def binSrch(self,arr, low, high, x):
        mid = (high + low) // 2
        if high >= low: 
            if arr[mid] >= x: 
                return self.binSrch(arr, low, mid - 1, x) 
            else: 
                return self.binSrch(arr, mid + 1, high, x) 
        else: 
            return mid+1
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        location = self.binSrch(nums,0,(len(nums)-1),target)
        return location
        
    
        
