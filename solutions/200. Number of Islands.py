# Classic Union Find DS
class UnionFind:
    
    def __init__(self,m,n):
        self.parent = [0]*(m*n)
        self.size = [1]*(m*n)
        
        # initally root is itself
        for i in range(m*n):
            self.parent[i] = i
            
    # classic Find
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    
    def union(self, x, y):
        px,py = map(self.find, [x,y])
        
        # if same root no need to join
        if px == py:
            return
        
        # if px greater than insert to py
        if self.size[px] < self.size[py]:
            self.parent[px] = self.parent[py]
        
        # if py greater than insert to px
        elif self.size[px] > self.size[py]:
            self.parent[py] = self.parent[px]
            
        # if same then get to one of the roots
        # and then increment that root that got bigger
        else:
            self.parent[px] = self.parent[py]
            self.size[py]+=1
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
