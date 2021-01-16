class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

def maxMeeting(l,n):
    finalMettings=[]
    l.sort(key=lambda x:x.end)
    finalMettings.append(l[0].pos)
    time_limit = l[0].end
    for i in range(1, n):
        if l[i].start > time_limit:
            finalMettings.append(l[i].pos)
            time_limit = l[i].end
    for i in finalMettings:
        print(i + 1, end=" ")
    print()


if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5,10]
    f = [2, 4, 6, 7, 9, 9,11]
    n = len(s)
    l = []
    for i in range(n):
        l.append(meeting(s[i], f[i], i))
    maxMeeting(l, n)