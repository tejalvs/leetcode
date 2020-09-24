class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        spltStr=list(s)
        spltStr.sort()
        freq={}
        for i in spltStr:
            if i in freq.keys():
                freq[i]+=1
            else:
                freq[i]=1
        result=''
        sorted_dict = dict(sorted(freq.items(), key=operator.itemgetter(1),reverse=True))
        print(sorted_dict)
        for i in sorted_dict.keys():
            count=sorted_dict[i]
            for j in range(0,count):
                result=result+i
        print(result)
        return(result)'''
    
        dict_char = dict()
        
        count = collections.Counter(s)
        
        list_str = []
        
        for letter, frequency in count.most_common():
            list_str.append(letter*frequency)
            
        return "".join(list_str)
        
       
​
                
            
                
