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

# if __name__ == "__main__":
#     h = [52,1,2,5,44,6,7,8]
#     insertion_sort(h)
#     print(h)