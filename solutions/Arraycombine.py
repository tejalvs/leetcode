def combine_arrays(a,b):
    map={}
    for i in range(0,len(a)):
        if a[i] in map.keys():
            map[a[i]]+=1
        else:
            map[a[i]]=1
    for i in range(0,len(b)):
        if b[i] in map.keys():
            if b.count(b[i])<=map[b[i]]:
                continue
            else:
                diff=abs(b.count(b[i])-map[b[i]])
                map[b[i]] += diff
        else:
            map[b[i]] = 1
    print(map)




def Main():
    a=[1, 1, 2, 2, 2, 3, 3]
    b=[1, 1, 2, 2, 3]
    combine_arrays(a,b)


Main()