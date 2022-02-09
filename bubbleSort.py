def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

def selectionSort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i +1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if i != min_index:
            temp = list[i]
            list[i] = list[min_index]
            list[min_index] = temp
    return list

def insertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while temp < list[j] and j > -1:
            list[j+1] = list[j]
            list[j] = temp
            j -= 1
    return list

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i +=1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i +=1
    while j < len(list2):
        combined.append(list2[j])
        j +=1
    return combined

def mergeSort(list):
    if len(list) == 1:
        return list
    mid = int(len(list)/2)
    left = list[:mid]
    right = list[mid:]
    return merge( mergeSort( left ), mergeSort( right ) )

def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def pivot(list, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if list[i] < list[pivotIndex]:
            swapIndex +=1
            swap(list, swapIndex, i)
    swap(list, pivotIndex, swapIndex)
    return swapIndex

def quickSortHelper(list, left, right):
    if left < right:
        pivotIndex = pivot(list, left, right)
        quickSortHelper(list, left, pivotIndex-1)
        quickSortHelper(list, pivotIndex+1, right)
    return list

def quickSort(list):
    return quickSortHelper(list, 0, len(list)-1)

print(quickSort([4,6,1,6,4,8,3,9,2,6,5,88,7,3,2,5]))