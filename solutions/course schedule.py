def courseSchedule(course):
    course_Map=generateCourseMap(course)
    keylist=course_Map.keys()
    print(keylist)
    print(course_Map)
    result={}
    visited=[]
    for i in keylist:
        start=i
        end=''
        temp=course_Map[i]
        visited.append(i)
        while (len(temp)!=0):
            currentkey=temp.pop(0)
            print(i,currentkey,temp)
            if currentkey in visited:
                continue
            visited.append(currentkey)
            if currentkey in keylist:
                temp=temp+course_Map[currentkey]
            elif currentkey not in keylist:
                end=currentkey
                if start in result.keys():
                    result[start].append(end)
                else:
                    result[start]=[end]
    print(result)

def generateCourseMap(course):
    course_Map = {}
    for i in course:
        if i[0] in course_Map.keys():
            temp = course_Map[i[0]]
            temp.append(i[1])
            course_Map[i[0]] = temp
        else:
            course_Map[i[0]] = [i[1]]
    return course_Map

def Main():
    course=[['A','B'],['A','C'],['B','K'],['C','K'],['L','M'],
                ['L','N'],['D','E'],['D','J'],['E','F'],['E','G'],['F','H'],['G','I']]
    courseSchedule(course)

Main()