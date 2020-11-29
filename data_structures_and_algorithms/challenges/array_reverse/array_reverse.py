def reverse_array_3(arr):
    return arr[::-1]

def reverse_array_2(arr):
    res=[]
    for i in arr:
        res.insert(0,i)
    return res

def reverse_array(arr):
    res=[]
    x=1
    while x <len(arr)+1:
        res.append(arr[len(arr)-x])
        x+=1
    return res

