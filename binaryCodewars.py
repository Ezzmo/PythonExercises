def first_non_consecutive(arr):
    nonconsec=[]
    for i in range(len(arr)+1):
        if arr[i] != arr[i+1]-1:
            nonconsec.append(arr[i+1])
            print(nonconsec)
    if len(nonconsec) == 0:
        return(None)
    else:
        return(nonconsec[0])

print(first_non_consecutive([1,2,3,4,5]))