def remove_elements(lista):
    # Creamos una copia para no modificar la lista original
    nueva_lista = lista[:]
    # Eliminamos los elementos si existen, desde el último al primero para no cambiar los índices
    for i in sorted([0, 4, 5], reverse=True):
        if i < len(nueva_lista):
            del nueva_lista[i]
    return nueva_lista

def add_elements(lista):
    nueva_lista = lista[:]
    nueva_lista.insert(0, 'Pink')  # Insertamos al principio
    nueva_lista.append('Yellow')   # Agregamos al final
    return nueva_lista

def is_empty(lista):
    return len(lista) == 0

def check_lists(lista1, lista2):
    if len(lista1) >= 3 and len(lista2) >= 3:
        return lista1[2] == lista2[2]
    else:
        return False

def list_of_lists(lista_de_listas):
    nueva_lista = []
    # Primera sublista: primeros 2 elementos
    if len(lista_de_listas[0]) >= 2:
        nueva_lista.append(lista_de_listas[0][:2])
    else:
        nueva_lista.append(lista_de_listas[0][:])

    # Segunda sublista: del segundo al cuarto (índices 1 a 3)
    if len(lista_de_listas[1]) >= 4:
        nueva_lista.append(lista_de_listas[1][1:4])
    else:
        nueva_lista.append(lista_de_listas[1][1:])

    # Tercera sublista: últimos 2 elementos
    nueva_lista.append(lista_de_listas[2][-2:])
    
    return nueva_lista
