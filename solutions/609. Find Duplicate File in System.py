class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentSet=dict()
        for path in paths:
            current_path=path.split(" ")
            for file in range(1,len(current_path)):
                path=current_path[0]
                start=current_path[file].find('(')
                end=current_path[file].find(')')
                path=path+"/"+current_path[file][:start]
                contentSet[path]=current_path[file][start+1:end]
        groupedSet={}
        for k,v in contentSet.items():
            if v not in groupedSet:
                groupedSet[v]=[k]
            else:
                groupedSet[v].append(k)
        finalList=[]
        for k,v in groupedSet.items():
            if len(v)>1:
                finalList.append(v)
        print(contentSet)
        print(groupedSet)
       
        if len(groupedSet)<len(contentSet):
            return finalList
        elif len(groupedSet)==len(contentSet):
            return[]
