'''Split the given text into words
Firstly select the words which can be inserted in each line including a space between each word.
For that, the sum of length of included words with one space between them must be smaller than or equal to L.
Now count the number of spaces needed to make the length of each line L and distribute the spaces evenly.
Repeat above steps for next set of words.
For the last line spaces must be assigned at the end as the last line must be left-justified.'''
def getLines(sample,k):
    sample_edit = sample.replace('\n', '')
    words = sample_edit.split()
    line = []
    count = 0
    end = 0
    start = 0
    for i in range(len(words)):
        count += len(words[i]) + 1
        end = i
        if count >= k:
            line.append(" ".join(words[start:end]))
            count = len(words[end]) + 1
            start = end
    line.append("-".join(words[start:end + 1]))
    return line

def addSpace(line,diff):
    counter=line.count('-')
    if counter==0:
        return line
    elif counter==1:
        element=line.split('-')
        diff=diff+1
        s="-"*diff
        line=s.join(element)
        return line
    else:
        diff=diff+line.count('-')
        element=line.split('-')
        index=0
        while(diff>0):
            element[index]=element[index]+'-'
            diff-=1
            index+=1
            if index>=(len(element)-1):
                index=0
        return "".join(element)





def justify(line,k):
    for i in range(0, len(line)):
        line[i]=line[i].replace(" ","-")
        cnt=line[i].count('-')
        if cnt<k:
            diff=k-len(line[i])
            line[i]=addSpace(line[i],diff)
    return line

def reflow(sample,k):
    line=getLines(sample,k)
    print(justify(line,k))





reflow('Geeksfor Geek is \nthe best \ncomputer science \nportal \nfor geeks.',16)
