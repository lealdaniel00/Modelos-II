def invertir(lista):
    if(len(lista)-1<=0):
        return lista[len(lista)-1:len(lista)]
    else:
        return lista[len(lista)-1:len(lista)]+invertir(lista[0:len(lista)-1])

def menoresMultilistas(lista):
    if(lista[0]>lista[1]):
        if(len(lista)<=2):
            return lista[1]
        else:
            return menoresMultilistas(lista[1:])
    else:
        if(len(lista)<=2):
            return lista[0]
        else:
            return menoresMultilistas(lista[0:1]+lista[2:])

def listadelista(lista):
    if(len(lista)<=1):
        return [menoresMultilistas(lista[0])]
    else:
        return [menoresMultilistas(lista[0])]+listadelista(lista[1:len(lista)])

def contar(lista):
    if(len(lista)<=0):
        return 0
    for i in lista:
        if i[0] == 'J' or  i[0] == 'K' or  i[0] == 'Q':
            return 10+contar(lista[1:])
        elif i[0] == 'A':
            if(contar(lista[1:])+11>=21 or contar(lista[1:])+11<=21):
                return contar(lista[1:])+11
            else:
                return contar(lista[1:])+1
        else:
            return i[0]+contar(lista[1:])
        
lista = [[5,4],[20,5],['A',5],[1,5]]
print (contar(lista))
