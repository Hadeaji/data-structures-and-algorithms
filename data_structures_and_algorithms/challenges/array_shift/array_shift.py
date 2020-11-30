import math

def insertShiftArray(arr,value):
    if type(value) != int:
        return 'Please Insert A Number'
    if type(arr) != list:
        return 'Please Insert An Array'
    i= math.ceil(len(arr)/2)
    return(arr[:i]+[value]+arr[i:])


