# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for x in range(len(arr)-1,0,-1):
        for i in range(x):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
array = [1, 5, 8, 2, 9, 4, 6, 3, 7, 0]
print(selection_sort(array))
def bubble_sort( arr ):
    return selection_sort(arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr