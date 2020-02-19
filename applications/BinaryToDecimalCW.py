def binary_array_to_number(arr):
    num=0
    arr.reverse()
    print(arr)
    for i, value in enumerate(arr):
        num += (2**i)*value
    return num

print(binary_array_to_number([1,0,0,1,1]))