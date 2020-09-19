class Solution:
    def removeVowels(self, S: str) -> str:
        ''' vowels=['a','e','i','o','u']
        print ("Original String : " + S) 
        for char in vowels:
            S=S.replace(char,'')
        print ("Resultant list is : " + str(S)) 
        return S''' 
        S=S.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
        return S
​
      
​
​
    
​
​
    
    
​
