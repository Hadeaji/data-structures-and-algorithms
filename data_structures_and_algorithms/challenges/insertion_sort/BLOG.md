# Insertion Sort

Insertion Sort is a sorting algorithm that traverses the array multiple times as it slowly builds out the sorting sequence

so first of all you get the length of the array

inside a loop:

you assgin a variable for the index 0

then you assign a variable for the one after

then check which one is bigger and swap their locations if required

this will only swap all values by one step of they apply the statment, **so what do we do?**

you guessed it right, nested loops

just assign the variables inside the first loop and outside the next one

do the statments inside and dont forget to iterrate to next values inside the loop after the statment

Trace:

Sample array: [8,4,23,42,16,15]


example code:

```
def insertion_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_ = i
        j=i+1
        for f in range(n-1):
            if arr[j] < arr[min_]:
                min_ = j
            j +=1
            if j > n-1:
                break

        temp = arr[min_]
        arr[min_] = arr[i]
        arr[i] = temp
```

![image](../../../assets/b1.jpg)

![image](../../../assets/b2.jpg)

![image](../../../assets/b3.jpg)

![image](../../../assets/b4.jpg)

![image](../../../assets/b5.jpg)
