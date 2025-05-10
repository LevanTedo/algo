import random

def swap(l,i,j):
    dummy = l[i]
    l[i] = l[j]
    l[j] = dummy

def quicksort(list,pivot1=0,pivot2=None): #Defaultwerte, welche bei rekursiven aufruf grenzen der teillisten darstellen können
    if pivot2 is None:
        pivot2 = len(list) - 1

    start = pivot1 #Info zur range des vorherigen Aufrufes von quicksort
    end = pivot2

    rightToLeft = True # bestimmt welcher pivot sich auf den anderen zubewegt
    if pivot1 == pivot2: # um unendliche rekursion zu vermeiden, wird bei funktionsaufruf auf leere liste hier abgebrochen
        return
    
    while pivot1 != pivot2: #solange pivots nicht an gleicher stelle sind, wird geswapped
        if list[pivot1] > list[pivot2]:
            swap(list,pivot1,pivot2)
            if rightToLeft == True: # ändert welcher pivot sich auf welchen zubewegt, nach swap
                rightToLeft = False
            else:
                rightToLeft = True
        if rightToLeft == True:
            pivot2 -= 1
        else:
            pivot1 += 1

    if pivot2 != 0: # dies vermeidet unendliche rekursion auf leeren listen
        quicksort(list,0,pivot2-1)# teilliste links vom pivot

    quicksort(list,start+1,end) # teilliste rechts vom pivot


def createRandomList(amount): # zum testen
    result= []
    for x in range(amount):
        subresult = []
        for y in range(10):
            subresult.append(random.randint(-20,20))
        result.append(subresult)
    return result

lists = createRandomList(10)

for x in range(len(lists)):
    print("Unsorted: ", lists[x])
    quicksort(lists[x])
    print("Sorted: ", lists[x])