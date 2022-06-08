import random


def getIndex(a, arr):
    for i in range(len(arr)):
        if a == arr[i]:
            return i
        
    return False


def mapElements(a1, a2, a3, b1, b2, b3):
    for i in range(len(a1)):
        if a1[i] in a2:
            curr = getIndex(a1[i], a2)
            while getIndex(b2[curr], a2):
                curr = getIndex(b2[curr], a2)
            a1[i] = b2[curr]
            
    for i in range(len(a3)):
        if a3[i] in a2:
            curr = getIndex(a3[i], a2)
            while getIndex(b2[curr], a2):
                curr = getIndex(b2[curr], a2)
            a3[i] = b2[curr]
            
    for i in range(len(b1)):
        if b1[i] in b2:
            curr = getIndex(b1[i], b2)
            while getIndex(a2[curr], b2):
                curr = getIndex(a2[curr], b2)
            b1[i] = a2[curr]
            
    for i in range(len(b3)):
        if b3[i] in b2:
            curr = getIndex(b3[i], b2)
            while getIndex(a2[curr], b2):
                curr = getIndex(a2[curr], b2)
            b3[i] = a2[curr]
       

def cross(arr1, arr2):
    point1 = random.randint(0, len(arr1) - 2)
    point2 = random.randint(point1 + 1, len(arr1) - 1)
    
    a1 = arr1[:point1]
    a2 = arr1[point1:point2]
    a3 = arr1[point2:]

    b1 = arr2[:point1]
    b2 = arr2[point1:point2]
    b3 = arr2[point2:]

    mapElements(a1, b2, a3, b1, a2, b3)
    
    return [a1 + b2 + a3, b1 + a2 + b3]
    

    


