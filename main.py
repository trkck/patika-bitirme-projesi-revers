

#liste elemanlarını tersine çeviren elemanlarından liste olan varsa onlarında yani nested listelerinde
#elemanlarını da tersine çeviren program
def rev(l):
    l.reverse()
    for i in range(len(l)):
        if type(l[i]) == list:
            l[i].reverse()

    return l

bosliste = []
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]