import sys
def long_subs(s1, s2):
    m=len(s1)
    n=len(s2)
    table = [[0 for x in range(n+1)] for x in range (m+1)]
    for i in range (m+1):
        for j in range (n+1):
            if i==0 or j==0:
                table[i][j]=0
            elif s1[i-1]==s2[j-1]:
                table[i][j]=1 + table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j], table[i][j-1])
    return table[m][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    assert 1<=n<=100
    assert 1<=m<=100
    for i in a:
        assert -10**9<i<10**9
    for i in b:
        assert -10**9<i<10**9
    print(long_subs(a, b))
