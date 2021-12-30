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

print(selectionSort([6,3,6,1,12,54,2,8,3,7,3]))