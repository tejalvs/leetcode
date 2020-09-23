​
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count={}
        result=[]
        for w in words:
            if w in count:
                count[w]+=1
            else:
                count[w]=1
        sorted_d = dict(sorted(count.items(), key=operator.itemgetter(1),reverse=True))
        print(sorted_d)
        counter=0
        for key,value in sorted_d.items():
            if counter!=k:
                result.append(key)
                counter+=1
            else:
                break
        print(result)
        return result
