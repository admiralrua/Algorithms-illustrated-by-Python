import sys
sys.setrecursionlimit(1000000)

def merge(aL, aR):
    aS, nL, nR, i, j = [], len(aL), len(aR), 0, 0
    
    while (i < nL) and (j < nR):
        if (aL[i] < aR[j]):
            aS.append(aL[i])
            i    += 1
        else:
            aS.append(aR[j])
            j    += 1
            
    for i in range(i,nL):
        aS.append(aL[i])
        
    for j in range(j,nR):
        aS.append(aR[j])
        
    return aS


def mergeSort(a):
    n  = len(a)-1
    
    if (n == 0):
        return a
    
    nL = int(n/2)
    
    aL = a[0:nL+1]
    aR = a[nL+1:n+1]
    
    aL = mergeSort(aL)
    aR = mergeSort(aR)
    
    a = merge(aL, aR)
    return a    

