class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        highest=0
        for acc in accounts:
            currentSum=0
            for i in acc:
                currentSum=currentSum+i
            if currentSum> highest:
                highest=currentSum
        return highest
        
        
