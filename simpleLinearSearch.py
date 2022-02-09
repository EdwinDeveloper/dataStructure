from tkinter.messagebox import NO


def linear_search(list, tarject):
    for i in range(0, len(list)):
        if list[i] == tarject:
            return i
    return None

def verify_result(index):
    if index is None:
        print("Elemento no existente dentro de la lista")
    else:
        print("Elemento en pa posición {}".format(index))

verify_result(linear_search([2,5,6,7,9,10],9))