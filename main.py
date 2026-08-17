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

while actual is not None:
    print(actual.value)
    actual = actual.next