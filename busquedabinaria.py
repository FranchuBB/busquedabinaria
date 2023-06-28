############ Busqueda Binaria #########################
######## SOLO SIRVE EN LISTAS OREDNADAS ###############


lista= [1,2,3,4,5,6,7,8,9,10,11,12]
num= int(input("numero a buscar: "))

def busquedabinaria(lista, num):
    pos = -1
    inferior= 0
    superior = len(lista)-1
    while inferior <= superior and pos == -1:
        mitad= (inferior+superior) // 2  # idivision que solo da entero
        if lista[mitad] == num:
            pos = mitad
        elif lista[mitad] < num:
                inferior = mitad +1
        else: 
            superior = mitad - 1
    return pos +1

print(busquedabinaria(lista, num))