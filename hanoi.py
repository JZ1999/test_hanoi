def hanoi(n):
    columnas = [list(range(1,n+1)),[],[]]
    print(operacion(columnas,n))

def operacion(col,n):
    res = ""
    contador = 0
    while(True):
        if contador==2**n-1:break
        if contador%3==1:
            puedeMoverse(col[1],col[2])
        elif contador%3==2:
            puedeMoverse(col[0],col[2])
        elif contador%3==0:
            puedeMoverse(col[0],col[1])
        res+=imprimir(col)
        contador+=1

    return res

def puedeMoverse(col1, col2):
    print(col1,col2)
    if len(col1)==0: 
        col1.insert(0,col2.pop(0))
    elif len(col2)==0:
        col2.insert(0,col1.pop(0))
    elif col1[0] > col2[0]:
        col1.insert(0,col2.pop(0))
    else:
        col2.insert(0,col1.pop(0))


def imprimir(col):
    out = ""
    out+="\n=======\n"
    out+="\nBorigen "+str(col[0])+"\n"
    out+="\nBcentro "+str(col[1])+"\n"
    out+="\nBdestino "+str(col[2])+"\n"
    out+="\n=======\n"
    return out

if __name__ == "__main__":
    hanoi(4)
