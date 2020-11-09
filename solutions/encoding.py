import sys
def encoding(x):
    encoding={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',
             14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
    
    number=int(x)
    result=[]
    if number<=26 and number>9:#numbers below 26
        result.append(encoding[number])
        soln=''
        while(number>0):
            rem=number%10
            number=number//10
            soln=soln+encoding[rem]
        result.append(soln)
            
    number=int(x)
    if len(x)>2 and number >26 :#all numbers above 26: get the individaula digits and find its respective encoding
        soln=''
        while(number>0):
            rem=number%10
            number=number//10
            soln=encoding[rem]
            result.append(soln)
      
    print(len(result))

encoding('20')