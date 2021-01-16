'''Given a list of historic stock prices, write a function that tells when you should have bought and sold to make the most profit.
You can only buy and sell once.'''

def MaxProfit():
    print()

def stockPrice(stocks,start,end):
    if end<=start:
        return 0
    maxprofit=0
    for i in range(start,end,1):
        for j in range(i+1,end+1):
            print()



def Main():
    price = [100, 180, 260, 310, 40, 535, 695]
    n = len(price)
    stockPrice(price,0,n-1)
