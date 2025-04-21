L = [1,1,1,2,2,3,4,5,6,6,7,8,9,10]

def removeDuplicates(L):
    """Diese Funktion nimmt eine sortierte Liste L mit mehrfach vorkommenden Zahlen 
        und erstellt eine Ergebnisliste result. Der erste Wert von L wird direkt übernommen
        und bei den folgenden Werten wird geprüft, ob der Wert dem aktuellsten Wert in der result-Liste
        gleicht. Sollte dies nicht der Fall sein, wird der Wert aus L der result-Liste hinzugefügt."""
    result = []
    for x in L:
        if len(result)==0: 
            result.append(L[0])
        else:
            if x != result[len(result)-1]:
                result.append(x)
    return result
    

print(removeDuplicates(L))
    
    
        
