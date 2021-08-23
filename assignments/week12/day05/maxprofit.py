def maxprofit(prices):

    maxcurr = maxsofar = 0

    for i in range (1 , len(prices)):

        maxcurr += prices[i] - prices[i-1]
        maxcurr = max (maxcurr , 0)

        maxsofar = max (maxsofar , maxcurr)

    return maxsofar


if __name__ == '__main__':

    prices = [2,6,3,6,1,9,6]
    print(maxprofit(prices))

