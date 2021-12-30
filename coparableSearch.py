def searchIneficient(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

def searchEficient(list1, list2):
    my_dic = {}
    for i in list1:
        my_dic[i] = True
    
    for j in list2:
        if j in my_dic:
            return True
    return False

list1 = [1, 2, 5]
list2 = [3, 4, 5]

print(searchEficient(list1, list2))
