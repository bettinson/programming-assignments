#Matt Bettinson
#10138240


def algorithmA(lis, target):
    for x in lis:
        if x == target:
            return True
    return False

def algorithmB(lis, target):
    sortedLis = quickSort(lis)
    

def quickSort(lis):
    less = []
    equal = []
    greater = []
    size = len(lis)
    if size > 1:
        pivot = lis[size // 2]
        for i in lis:
            if i > pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i < pivot:
                greater.append(i)
        less = quickSort(less)
        greater = quickSort(greater)
        lis = greater + equal + less
    return lis

