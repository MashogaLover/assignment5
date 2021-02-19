import numpy as np
def Casteljau(P_0, t_0):
    n = len(P_0)
    P_ij = [P_0]
    for j in range(1,n+1):
        P_temp = []
        for i in range(0, n-j+1):
            #print(n-j+1)
            P_temp.append(P_ij[j-1][i]*(1-t_0)+P_ij[j-1][i])
        print(P_temp,len(P_temp),n-j+1,'x')
        P_ij.append(P_temp)
        print("")
    return P_ij[n-1][0]
print(Casteljau([[0,1],[0,0],[0,1],[1,1],[1,1],[1,1]], 0))
