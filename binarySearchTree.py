class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: 
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node
    
    def min_value(self):
        prev = self.root
        temp = self.root
        while temp is not None:
            prev = temp
            temp = temp.left
        return prev

    def max_value(self):
        prev = self.root
        temp = self.root
        while temp is not None:
            print(temp.value)
            prev = temp
            temp = temp.right
        return prev 
        

my_tree = BinarySearchTree()
print("1")
for i in range(9999):
     print("Numero : ", i)
     my_tree.insert(i)
print("Saliendo")
my_tree.max_value()