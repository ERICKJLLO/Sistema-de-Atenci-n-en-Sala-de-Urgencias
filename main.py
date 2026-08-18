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


if __name__ == "__main__":
    punto_1()
    punto_2(construir_lista_base())
    punto_3(construir_lista_base())
