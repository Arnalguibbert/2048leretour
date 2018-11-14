
def move_row_left(L):
    n=len(L)
    for j in range(0,n):
        i=j
        while L[i]==0 and i<=n-1:
            i+=1
        L[j]=L[i]
    for k in range(0,n-1):
        if L[k]==L[k+1]:
            L[k]=L[k+1]
            L[k+1]=0
    for j in range(0,n):
        i=j
        while L[i]==0 and i<=n-1:
            i+=1
        L[j]=L[i]
    return L


