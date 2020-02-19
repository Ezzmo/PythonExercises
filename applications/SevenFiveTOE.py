def sevenfivedivision(n,m):
    solutionarray=[]
    for i in range(n,m):
        if i%5!=0 and i%7==0:
            solutionarray.append(i)
    stringsol=str(solutionarray).strip('[]')
    return stringsol
