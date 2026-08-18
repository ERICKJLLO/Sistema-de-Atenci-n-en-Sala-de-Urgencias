from paciente import Paciente
from lista_doblemente_enlazada import dlinkedlist


def mostrar_lista(etiqueta, lista):
    print(etiqueta)
    actual = lista.head
    if actual is None:
        print("Lista vacía")
    else:
        while actual is not None:
            print(actual.value)
            actual = actual.next
    print()


def construir_lista_base():
    lista = dlinkedlist()
    lista.append(Paciente("P-101", "tercera_edad", 1))
    lista.append(Paciente("P-102", "adulto", 4))
    lista.append(Paciente("P-103", "pediatria", 2))
    lista.append(Paciente("P-104", "adulto", 2))
    lista.append(Paciente("P-105", "tercera_edad", 1))
    lista.append(Paciente("P-106", "pediatria", 3))
    lista.append(Paciente("P-107", "adulto", 5))
    lista.append(Paciente("P-108", "tercera_edad", 2))
    lista.append(Paciente("P-109", "adulto", 4))
    lista.append(Paciente("P-110", "pediatria", 1))
    lista.append(Paciente("P-111", "adulto", 3))
    lista.append(Paciente("P-112", "tercera_edad", 2))
    return lista


def punto_1():
    lista = dlinkedlist()
    lista.append(Paciente("P-101", "tercera_edad", 1))
    lista.append(Paciente("P-102", "adulto", 4))
    lista.append(Paciente("P-103", "pediatria", 2))
    lista.append(Paciente("P-104", "adulto", 2))
    print("Punto 1")
    mostrar_lista("Lista después de registrar pacientes al final:", lista)
    return lista


def punto_2(lista):
    if lista.head is None:
        print("Punto 2")
        mostrar_lista("Lista vacía, no se mueve ningún paciente:", lista)
        return lista

    head_prioritarios = None
    tail_prioritarios = None
    actual = lista.head

    while actual is not None:
        siguiente = actual.next
        if actual.value.categoria == "tercera_edad" and actual.value.nivel_triage == 1:
            if actual.prev is not None:
                actual.prev.next = siguiente
            else:
                lista.head = siguiente

            if siguiente is not None:
                siguiente.prev = actual.prev
            else:
                lista.tail = actual.prev

            actual.prev = None
            actual.next = None

            if head_prioritarios is None:
                head_prioritarios = actual
                tail_prioritarios = actual
            else:
                tail_prioritarios.next = actual
                actual.prev = tail_prioritarios
                tail_prioritarios = actual
        actual = siguiente

    if head_prioritarios is not None:
        if lista.head is not None:
            lista.head.prev = tail_prioritarios
            tail_prioritarios.next = lista.head
        else:
            lista.tail = tail_prioritarios
        head_prioritarios.prev = None
        lista.head = head_prioritarios

    print("Punto 2")
    mostrar_lista("Lista después de mover pacientes de tercera_edad con triage 1 al inicio:", lista)
    return lista


def punto_3(lista):
    actual = lista.head
    while actual is not None:
        siguiente = actual.next
        if actual.value.categoria == "adulto" and actual.value.nivel_triage > 3:
            if actual.prev is not None:
                actual.prev.next = siguiente
            else:
                lista.head = siguiente

            if siguiente is not None:
                siguiente.prev = actual.prev
            else:
                lista.tail = actual.prev

            actual.prev = None
            actual.next = None
        actual = siguiente

    print("Punto 3")
    mostrar_lista("Lista después de depurar adultos con triage mayor a 3:", lista)
    return lista


def punto_4(lista):
    lista_aislamiento = dlinkedlist()
    inicio = lista.find_by_id("P-103")
    fin = lista.find_by_id("P-109")

    if inicio is None or fin is None:
        print("Punto 4")
        mostrar_lista("Lista principal sin cambios porque alguno de los IDs no existe:", lista)
        mostrar_lista("Lista de aislamiento vacía:", lista_aislamiento)
        return lista, lista_aislamiento

    primer = inicio
    ultimo = fin
    actual = inicio
    while actual is not None and actual is not fin:
        actual = actual.next
    if actual is not fin:
        actual = fin
        while actual is not None and actual is not inicio:
            actual = actual.next
        if actual is not inicio:
            print("Punto 4")
            mostrar_lista("Lista principal sin cambios porque los IDs no están en la misma lista:", lista)
            mostrar_lista("Lista de aislamiento vacía:", lista_aislamiento)
            return lista, lista_aislamiento
        primer = fin
        ultimo = inicio

    if primer.next is ultimo or primer is ultimo:
        print("Punto 4")
        mostrar_lista("Lista principal sin cambios porque no hay nodos intermedios:", lista)
        mostrar_lista("Lista de aislamiento vacía:", lista_aislamiento)
        return lista, lista_aislamiento

    bloque_inicio = primer.next
    bloque_fin = ultimo.prev

    primer.next = ultimo
    ultimo.prev = primer

    if bloque_inicio is not None:
        bloque_inicio.prev = None
    if bloque_fin is not None:
        bloque_fin.next = None

    lista_aislamiento.head = bloque_inicio
    lista_aislamiento.tail = bloque_fin
    lista_aislamiento.size = 0
    actual = bloque_inicio
    while actual is not None:
        lista_aislamiento.size += 1
        actual = actual.next

    print("Punto 4")
    mostrar_lista("Lista principal después de aislar el tramo:", lista)
    mostrar_lista("Lista de aislamiento:", lista_aislamiento)
    return lista, lista_aislamiento


def punto_5(lista):
    cantidad_pediatria = 0
    cantidad_adulto = 0
    actual = lista.head
    while actual is not None:
        if actual.value.categoria == "pediatria":
            cantidad_pediatria += 1
        elif actual.value.categoria == "adulto":
            cantidad_adulto += 1
        actual = actual.next

    if cantidad_pediatria > cantidad_adulto:
        old_head = lista.head
        old_tail = lista.tail
        actual = lista.head
        while actual is not None:
            siguiente = actual.next
            actual.next = actual.prev
            actual.prev = siguiente
            actual = siguiente
        lista.head = old_tail
        lista.tail = old_head

    print("Punto 5")
    mostrar_lista("Lista después de la inversión condicional:", lista)
    return lista


def punto_6(lista):
    if lista.head is None:
        print("Punto 6")
        mostrar_lista("Lista vacía:", lista)
        return lista

    def prioridad(paciente):
        orden = {"tercera_edad": 0, "pediatria": 1, "adulto": 2}
        return (paciente.nivel_triage, orden[paciente.categoria])

    head_ordenado = lista.head
    lista.head = lista.head.next
    if lista.head is not None:
        lista.head.prev = None
    head_ordenado.next = None
    head_ordenado.prev = None

    actual = lista.head
    while actual is not None:
        siguiente = actual.next
        actual.prev = None
        actual.next = None
        cursor = head_ordenado
        prev = None

        while cursor is not None and prioridad(cursor.value) <= prioridad(actual.value):
            prev = cursor
            cursor = cursor.next

        if prev is None:
            actual.next = head_ordenado
            head_ordenado.prev = actual
            head_ordenado = actual
        else:
            actual.prev = prev
            actual.next = prev.next
            if prev.next is not None:
                prev.next.prev = actual
            prev.next = actual

        actual = siguiente

    lista.head = head_ordenado
    cursor = lista.head
    while cursor.next is not None:
        cursor = cursor.next
    lista.tail = cursor

    print("Punto 6")
    mostrar_lista("Lista reordenada por triage y categoría:", lista)
    return lista


def punto_7(lista, lista_derivados):
    if lista_derivados.head is None:
        print("Punto 7")
        mostrar_lista("No hay derivados para intercalar:", lista)
        mostrar_lista("Lista derivados vacía:", lista_derivados)
        return lista

    if lista.head is None:
        lista.head = lista_derivados.head
        lista.tail = lista_derivados.tail
        lista_derivados.clear()
        print("Punto 7")
        mostrar_lista("Lista principal después de recibir la lista derivada:", lista)
        mostrar_lista("Lista derivados vacía:", lista_derivados)
        return lista

    nueva_head = None
    nueva_tail = None
    anterior = None
    main_actual = lista.head
    deriv_actual = lista_derivados.head
    contador = 0

    while main_actual is not None:
        nodo = main_actual
        main_actual = main_actual.next
        nodo.prev = None
        nodo.next = None

        if nueva_head is None:
            nueva_head = nodo
        else:
            anterior.next = nodo
            nodo.prev = anterior
        anterior = nodo
        nueva_tail = nodo
        contador += 1

        if contador == 2 and deriv_actual is not None:
            nodo_derivado = deriv_actual
            deriv_actual = deriv_actual.next
            nodo_derivado.prev = None
            nodo_derivado.next = None
            anterior.next = nodo_derivado
            nodo_derivado.prev = anterior
            anterior = nodo_derivado
            nueva_tail = nodo_derivado
            contador = 0

    while deriv_actual is not None:
        nodo_derivado = deriv_actual
        deriv_actual = deriv_actual.next
        nodo_derivado.prev = None
        nodo_derivado.next = None
        anterior.next = nodo_derivado
        nodo_derivado.prev = anterior
        anterior = nodo_derivado
        nueva_tail = nodo_derivado

    lista.head = nueva_head
    lista.tail = nueva_tail
    lista_derivados.clear()

    print("Punto 7")
    mostrar_lista("Lista principal después del intercalado 2:1:", lista)
    mostrar_lista("Lista derivados vacía:", lista_derivados)
    return lista


if __name__ == "__main__":
    punto_1()
    lista_2 = construir_lista_base()
    punto_2(lista_2)
    lista_3 = construir_lista_base()
    punto_3(lista_3)
    lista_4 = construir_lista_base()
    punto_4(lista_4)
    lista_5 = construir_lista_base()
    punto_5(lista_5)
    lista_6 = construir_lista_base()
    punto_6(lista_6)

    lista_7 = construir_lista_base()
    lista_derivados = dlinkedlist()
    lista_derivados.append(Paciente("D-201", "adulto", 2))
    lista_derivados.append(Paciente("D-202", "pediatria", 1))
    lista_derivados.append(Paciente("D-203", "tercera_edad", 2))
    lista_derivados.append(Paciente("D-204", "adulto", 3))
    punto_7(lista_7, lista_derivados)    
