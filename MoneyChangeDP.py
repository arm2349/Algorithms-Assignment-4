import sys
def get_change(m):
    coin_values = [4,3,1]
    arr=[None for x in range (m+1)]
    arr[0]=0
    if m==0:
        return 0
    #arr[2]=2

    for coin in coin_values:
        if coin<=m:
            arr[coin]=1
        #else:
        #    arr[coin]=0

    for i in range (1, m+1):
        r=store_results(coin_values, arr, i)
    return r


def store_results(coin_values, arr, m):
    if (arr[m]==None):
        results=[m]*len(coin_values)
        for i in range(len(coin_values)):
            if (coin_values[i]>m):
                continue
            results[i]=1 + store_results(coin_values, arr, m-coin_values[i])
        arr[m]=min(results)
    return arr[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
