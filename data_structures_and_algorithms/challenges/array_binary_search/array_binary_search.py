import math

def BinarySearch(arr,key):
    test=arr[0]
    mid=int(math.floor((len(arr)/2)))
    indi=mid
    if type(key) != int:
        return 'Please Insert A Number'
    if type(arr) != list:
        return 'Please Insert An Array'
    while test != key:
        test=arr[mid]
        if test == key:
            return indi
        elif test > key:
            arr=arr[:mid]
            mid=int(math.floor((len(arr)/2)))
            if mid !=len(arr)/2:
                indi-=(mid+1)
            else:
                indi-=(mid)
        elif test < key:
            arr=arr[mid:]
            mid=int(math.floor((len(arr)/2)))
            if mid %2==0:
                indi+=(mid)
            else:
                indi+=(mid)
        if mid <=0:
            return 'Sorry Invailed Input'
