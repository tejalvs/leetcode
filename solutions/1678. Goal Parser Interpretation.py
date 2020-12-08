class Solution:
    def interpret(self, command: str) -> str:
        result=''
        testList=list(command)
        for i in range(len(testList)):
            if testList[i]=='G':
                result=result+testList[i]
                continue
            elif testList[i]=="(" and testList[i+1]==")":
                result=result+'o'
                i=i+1
                continue
            elif testList[i]=='a' and testList[i+1]=='l':
                result=result+testList[i]+testList[i+1]
                i=i+1
                continue
        return result
    
                
                
                
