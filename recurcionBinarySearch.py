def recursion_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursion_binary_search(list[midpoint+1:], target)
        else:
            return recursion_binary_search(list[:midpoint], target)
    
print(recursion_binary_search([0.1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], 10))