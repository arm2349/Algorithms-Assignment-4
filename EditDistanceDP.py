def edit_distanceDP(s1, s2):
    m=len(s1)
    n=len(s2)
    assert 1<=m<100
    assert 1<=n<100
    table = [[0 for x in range (n+1)] for x in range(m+1)]
    for i in range (m+1):
        for j in range (n+1):
            if i==0:
                table[i][j]=j
            elif j==0:
                table[i][j]=i
            elif s1[i-1] == s2[j-1]:
                table[i][j]=min(table[i-1][j-1], 1+table[i-1][j], 1+table[i][j-1])
            else:
                table[i][j] = 1 + min(table[i-1][j],
                                 table[i][j-1],
                                 table[i-1][j-1]
                                 )
    return int(table[m][n])

if __name__ == "__main__":
    print(int(edit_distanceDP(input(), input())))
