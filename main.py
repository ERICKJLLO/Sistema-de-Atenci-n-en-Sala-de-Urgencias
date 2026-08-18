from paciente import Paciente
from lista_doblemente_enlazada import dlinkedlist


lista_espera = dlinkedlist()

lista_espera.append(Paciente("P-101", "tercera_edad", 1))
lista_espera.append(Paciente("P-102", "adulto", 4))
lista_espera.append(Paciente("P-103", "pediatria", 2))
lista_espera.append(Paciente("P-104", "adulto", 2))
lista_espera.append(Paciente("P-105", "tercera_edad", 1))
lista_espera.append(Paciente("P-106", "pediatria", 3))
lista_espera.append(Paciente("P-107", "adulto", 5))
lista_espera.append(Paciente("P-108", "tercera_edad", 2))

actual = lista_espera.head

actual = lista_espera.head
ultimo_prioritario = None

while actual is not None:
    siguiente = actual.next

    if actual.value.categoria == "tercera_edad" and actual.value.nivel_triage == 1:

        if actual != lista_espera.head:

            anterior = actual.prev

            anterior.next = siguiente

            if siguiente is not None:
                siguiente.prev = anterior
            else:
                lista_espera.tail = anterior

            if ultimo_prioritario is None:
                actual.prev = None
                actual.next = lista_espera.head
                lista_espera.head.prev = actual
                lista_espera.head = actual
            else:
                siguiente_prioritario = ultimo_prioritario.next

                actual.prev = ultimo_prioritario
                actual.next = siguiente_prioritario

                ultimo_prioritario.next = actual

                if siguiente_prioritario is not None:
                    siguiente_prioritario.prev = actual
                else:
                    lista_espera.tail = actual

        ultimo_prioritario = actual

    actual = siguiente
    
print("\nDespués del Punto 2:")

actual = lista_espera.head

while actual is not None:
    print(actual.value)
    actual = actual.next