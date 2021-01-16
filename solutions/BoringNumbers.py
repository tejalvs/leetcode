def boringNumber(L,R):

    BoringList=set()
    for number in range(L,R+1,1):
        reversedNo = int(str(number)[::-1])
        digit = list(str(reversedNo))
        digit = [int(i) for i in digit]
        for i in range(len(digit)):
            if i % 2==0 :
                if digit[i]%2==0:
                    BoringList.add(number)
                    continue
                elif (digit[i]%2 !=0):
                    break
            elif i%2 !=0:
                if digit[i]%2!=0:
                    BoringList.add(number)
                    continue
                elif (digit[i]%2 !=0):
                    break
    print(BoringList)


boringNumber(19,30)


